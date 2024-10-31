#!/bin/bash
LIB_SRC="\$(LIB_SRC)"
script_octave="script_octave.m"

output_dir="0"
output_file="$output_dir/ID"
output_file2="$output_dir/corr"

cat > $script_octave << EOF
% Criação da figura

hFig = figure('Name', 'Malha Bidimensional', 'NumberTitle', 'off');

% Pergunta inicial sobre as dimensões da malha

prompt = {'Informe a largura da malha (m):', 'Informe a altura da malha (m):'};
dlgtitle = 'Dimensões da Malha';
dims = [1 1];
definput = {'0.09', '0.09'};
answer = inputdlg(prompt, dlgtitle, dims, definput);
mesh_width = str2double(answer{1});
mesh_height = str2double(answer{2});


% Pergunta sobre a quantidade de tumores

prompt = {'Quantos tumores deseja inserir?'};
dlgtitle = 'Número de Tumores';
dims = [1 35];
definput = {'1'};
answer = inputdlg(prompt, dlgtitle, dims, definput);
num_tumors = str2double(answer{1});

% Inicialização de variáveis globais para armazenar dados dos tumores

global tumors;
tumors = struct('shapeType', [], 'radius', [], 'eccentricity', [], 'inclination', [], 'x', [], 'y', []);

for i = 1:num_tumors
    % Pergunta sobre a forma e a posição do tumor
    shapeChoice = questdlg(sprintf('Escolha o formato do tumor %d:', i), 'Forma', 'Circular', 'Elíptica', 'Circular');
    prompt = {'Informe a posição X:', 'Informe a posição Y:'};
    dlgtitle = sprintf('Posição do Tumor %d', i);
    dims = [1 1];
    definput = {'0.045', '0.045'};
    answer = inputdlg(prompt, dlgtitle, dims, definput);
    posX = str2double(answer{1});
    posY = str2double(answer{2});

    if strcmp(shapeChoice, 'Circular')
        prompt = {'Informe o raio:'};
        dlgtitle = sprintf('Raio Circular do Tumor %d', i);
        dims = [1 35];
        definput = {'0.005'};
        answer = inputdlg(prompt, dlgtitle, dims, definput);
        radius = str2double(answer{1});
        eccentricity = 0;
        inclination = 0;
    else
        prompt = {'Informe a excentricidade:', 'Informe o raio do círculo equivalente:', 'Inclinação do tumor [°]'};
        dlgtitle = sprintf('Parâmetros Elípticos do Tumor %d', i);
        dims = [1 1 1];
        definput = {'0.9', '0.005', '0'};
        answer = inputdlg(prompt, dlgtitle, dims, definput);
        eccentricity = str2double(answer{1});
        radius = str2double(answer{2});
        inclination = str2double(answer{3});
    end
    
    % Armazena os dados do tumor
    tumors(i).shapeType = shapeChoice;
    tumors(i).radius = radius;
    tumors(i).eccentricity = eccentricity;
    tumors(i).inclination = inclination;
    tumors(i).x = posX;
    tumors(i).y = posY;
end
 
% Função para plotar os tumores

function plotShape(x, y, shapeType, radius, eccentricity, inclination)
    theta = linspace(0, 2*pi, 100);
    inclination_rad = pi*inclination/180; % Converte para radianos
    if strcmp(shapeType, 'Circular')
        % Plota um círculo
        xc = radius * cos(theta);
        yc = radius * sin(theta);
    else
        % Plota uma elipse
        adjustedRadius = radius / sqrt(1 - eccentricity^2);
        a = adjustedRadius;
        b = adjustedRadius * sqrt(1 - eccentricity^2);
        xc = a * cos(theta);
        yc = b * sin(theta);
        % Aplicar a rotação
        x_rot = xc * cos(inclination_rad) - yc * sin(inclination_rad);
        y_rot = xc * sin(inclination_rad) + yc * cos(inclination_rad);
        xc = x_rot;
        yc = y_rot;
    end
    fill(x + xc, y + yc, 'r', 'LineWidth', 2);
end

% Criação da malha bidimensional

X = linspace(0, mesh_width, 1);
Y = linspace(0, mesh_height, 1);
[xx, yy] = meshgrid(X, Y);
plot(xx, yy, 'k.');
grid on;
hold on;

% Configuração do eixo

axis([0 mesh_width 0 mesh_height]);
axis equal;
xlabel('X');
ylabel('Y');

% Plotagem dos tumores

for i = 1:num_tumors
    plotShape(tumors(i).x, tumors(i).y, tumors(i).shapeType, tumors(i).radius, tumors(i).eccentricity, tumors(i).inclination);
end

% Botão de confirmação

uicontrol('Style', 'pushbutton', 'String', 'Confirmar', 'Position', [20 20 100 30], 'Callback', 'uiresume(gcbf)');

% Aguarda confirmação

%uiwait(gbf);

% Mantém a janela aberta
lib_src_string = '-I${LIB_SRC}/finiteVolume/lnInclude \\';
lib_src_string2 ='-I${LIB_SRC}/meshTools/lnInclude ';
lib_src_string11 = '-lmeshTools \\';
lib_src_string22 ='-lfiniteVolume ';
waitfor(hFig);

waitfor(hFig);
fid = fopen('$output_file', 'w');

fprintf(fid, '/*--------------------------------*- C++ -*----------------------------------*|\n');
fprintf(fid, '| =========                 |                                                 |\n');
fprintf(fid, '| \\\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n');
fprintf(fid, '|  \\\\\    /   O peration     | Version:  2312                                  |\n');
fprintf(fid, '|   \\\\\  /    A nd           | Website:  www.openfoam.com                      |\n');
fprintf(fid, '|    \\\\\/     M anipulation  |                                                 |\n');
fprintf(fid, '|*---------------------------------------------------------------------------*/\n');
fprintf(fid, 'FoamFile\n{\n');
fprintf(fid, '    version     2.0;\n');
fprintf(fid, '    format      ascii;\n');
fprintf(fid, '    arch        "LSB;label=32;scalar=64";\n');
fprintf(fid, '    class       volScalarField;\n');
fprintf(fid, '    location    "0";\n');
fprintf(fid, '    object      ID;\n');
fprintf(fid, '}\n');
fprintf(fid, '// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n');
fprintf(fid, 'dimensions      [0 0 0 0 0 0 0];\n\n');
fprintf(fid, 'internalField #codeStream\n{\n');
fprintf(fid, '        codeInclude\n');
fprintf(fid, '        #{\n');
fprintf(fid, '                #include "fvCFD.H"\n');
fprintf(fid, '                #include "Ostream.H"\n');
fprintf(fid, '        #};\n\n');
fprintf(fid, '        codeOptions\n');
fprintf(fid, '        #{\n');
%fprintf(fid, '                -I$(LIB_SRC)/finiteVolume/lnInclude \\\n');
%fprintf(fid, '                -I$(LIB_SRC)/meshTools/lnInclude\n');
fprintf(fid, '                %s\n', lib_src_string);
fprintf(fid, '                %s\n', lib_src_string2);
fprintf(fid, '        #};\n');
fprintf(fid, '        codeLibs\n');
fprintf(fid, '        #{\n');
%fprintf(fid, '                -lmeshTools \\\n');
%fprintf(fid, '                -lfiniteVolume\n');
fprintf(fid, '                %s\n', lib_src_string11);
fprintf(fid, '                %s\n', lib_src_string22);
fprintf(fid, '        #};\n\n');
fprintf(fid, '        code\n');
fprintf(fid, '        #{\n\n');
fprintf(fid, '        const IOdictionary& d = static_cast<const IOdictionary&>(dict);\n');
fprintf(fid, '        const fvMesh& mesh = refCast<const fvMesh>(d.db());\n');
fprintf(fid, '        const scalar pi = 3.141592653589793;\n');
fprintf(fid, '        // Tumores\n');
fprintf(fid, '        scalarField ID(mesh.nCells(), 0.);\n');

for i = 1:num_tumors
    fprintf(fid, '        // Tumor %d\n', i);
    if strcmp(tumors(i).shapeType, 'Circular')
        fprintf(fid, '        scalar raiot%d = %.3f;\n', i, tumors(i).radius);
        fprintf(fid, '        scalar x%d = %.3f;\n', i, tumors(i).x);
        fprintf(fid, '        scalar y%d = %.3f;\n', i, tumors(i).y);
        fprintf(fid, '        scalar inclination_deg%d= %.3f;\n', i,tumors(i).inclination);
        fprintf(fid, '        scalar inclination_rad%d = inclination_deg%d * pi / 180.0;\n',i, i);
    else
        fprintf(fid, '        scalar raiot%d = %.3f;\n', i, tumors(i).radius);
        fprintf(fid, '        scalar ee%d = %.3f;\n', i, tumors(i).eccentricity);
        fprintf(fid, '        scalar be%d = raiot%d*pow((1-pow(ee%d,2)),0.25);\n', i, i, i);
        fprintf(fid, '        scalar ae%d = pow(pow(be%d,2)*(pow(1-pow(ee%d,2),-1)),0.5);\n', i, i, i);
        fprintf(fid, '        scalar x%d = %.3f;\n', i, tumors(i).x);
        fprintf(fid, '        scalar y%d = %.3f;\n', i, tumors(i).y);
        fprintf(fid, '        scalar inclination_deg%d= %.3f;\n', i,tumors(i).inclination);
        fprintf(fid, '        scalar inclination_rad%d = inclination_deg%d * pi / 180.0;\n',i ,i);
    end
end

fprintf(fid, '        forAll(ID, i)\n');
fprintf(fid, '        {\n');
fprintf(fid, '                const scalar x = mesh.C()[i][0];\n');
fprintf(fid, '                const scalar y = mesh.C()[i][1];\n');
fprintf(fid, '                const scalar z = mesh.C()[i][2];\n');
for i = 1:num_tumors
    fprintf(fid, '        scalar y_rot%d = (y - y%d) * cos(inclination_rad%d) - (x - x%d) * sin(inclination_rad%d);\n',i,i,i, i,i);
    fprintf(fid, '        scalar x_rot%d = (y - y%d) * sin(inclination_rad%d) + (x - x%d) * cos(inclination_rad%d);\n',i,i,i, i,i);
    if strcmp(tumors(i).shapeType, 'Circular')
        fprintf(fid, '                if ( pow(y-y%d,2) <= pow(raiot%d,2) - pow(x-x%d,2) )\n', i, i, i);
    else
        fprintf(fid, '                if ( pow(y_rot%d,2) <= ((1 - pow(x_rot%d,2)/pow(ae%d,2) )*pow(be%d,2)) )\n', i, i, i, i);
    end
    fprintf(fid, '                {\n');
    fprintf(fid, '                        ID[i] = 1.;\n');
    fprintf(fid, '                }\n');
end
fprintf(fid, '        }\n');
fprintf(fid, '        ID.writeEntry("", os);\n\n');
fprintf(fid, '        #};\n');
fprintf(fid, '};\n\n');
fprintf(fid, 'boundaryField\n{\n');
fprintf(fid, '    leftWall\n');
fprintf(fid, '    {\n');
fprintf(fid, '        type            fixedValue;\n');
fprintf(fid, '        value           uniform 0;\n');
fprintf(fid, '    }\n');
fprintf(fid, '    rightWall\n');
fprintf(fid, '    {\n');
fprintf(fid, '        type            fixedValue;\n');
fprintf(fid, '        value           uniform 0;\n');
fprintf(fid, '    }\n');
fprintf(fid, '    lowerWall\n');
fprintf(fid, '    {\n');
fprintf(fid, '        type            fixedValue;\n');
fprintf(fid, '        value           uniform 0;\n');
fprintf(fid, '    }\n');
fprintf(fid, '    upperWall\n');
fprintf(fid, '    {\n');
fprintf(fid, '        type            fixedValue;\n');
fprintf(fid, '        value           uniform 0;\n');
fprintf(fid, '    }\n');
fprintf(fid, '    defaultFaces\n');
fprintf(fid, '    {\n');
fprintf(fid, '        type            empty;\n');
fprintf(fid, '    }\n');
fprintf(fid, '}\n\n');
fprintf(fid, '// ************************************************************************* //\n');

fclose(fid);

fid2 = fopen('$output_file2', 'w');

fprintf(fid2, '/*--------------------------------*- C++ -*----------------------------------*|\n');
fprintf(fid2, '| =========                 |                                                 |\n');
fprintf(fid2, '| ||      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n');
fprintf(fid2, '|  ||    /   O peration     | Version:  2312                                  |\n');
fprintf(fid2, '|   ||  /    A nd           | Website:  www.openfoam.com                      |\n');
fprintf(fid2, '|    ||/     M anipulation  |                                                 |\n');
fprintf(fid2, '|*---------------------------------------------------------------------------*/\n');
fprintf(fid2, 'FoamFile\n{\n');
fprintf(fid2, '    version     2.0;\n');
fprintf(fid2, '    format      ascii;\n');
fprintf(fid2, '    arch        "LSB;label=32;scalar=64";\n');
fprintf(fid2, '    class       volScalarField;\n');
fprintf(fid2, '    location    "0";\n');
fprintf(fid2, '    object      corr;\n');
fprintf(fid2, '}\n');
fprintf(fid2, '// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n');
fprintf(fid2, 'dimensions      [0 0 0 0 0 0 0];\n\n');
fprintf(fid2, 'internalField #codeStream\n{\n');
fprintf(fid2, '        codeInclude\n');
fprintf(fid2, '        #{\n');
fprintf(fid2, '                #include "fvCFD.H"\n');
fprintf(fid2, '                #include "Ostream.H"\n');
fprintf(fid2, '        #};\n\n');
fprintf(fid2, '        codeOptions\n');
fprintf(fid2, '        #{\n');
%fprintf(fid2, '                -I$(LIB_SRC)/finiteVolume/lnInclude \\\n');
%fprintf(fid2, '                -I$(LIB_SRC)/meshTools/lnInclude\n');
fprintf(fid, '                %s\n', lib_src_string);
fprintf(fid, '                %s\n', lib_src_string2);
fprintf(fid2, '        #};\n\n');
fprintf(fid2, '        codeLibs\n');
fprintf(fid2, '        #{\n');
%fprintf(fid2, '                -lmeshTools \\\\n');
%fprintf(fid2, '                -lfiniteVolume\n');
fprintf(fid, '                %s\n', lib_src_string11);
fprintf(fid, '                %s\n', lib_src_string22);
fprintf(fid2, '        #};\n');
fprintf(fid2, '        code\n');
fprintf(fid2, '        #{\n\n');
fprintf(fid2, '        const IOdictionary& d = static_cast<const IOdictionary&>(dict);\n');
fprintf(fid2, '        const fvMesh& mesh = refCast<const fvMesh>(d.db());\n');
fprintf(fid2, '        scalarField corr(mesh.nCells(), 0.);\n');
fprintf(fid2, '	       \n');

for i = 1:num_tumors
    fprintf(fid2, '        // fluid magnetic on first tumor %d\n', i);
    if strcmp(tumors(i).shapeType, 'Circular')
        fprintf(fid2, '        scalar raiot%d = 0.00287;\n', i);
        fprintf(fid2, '        scalar x%d = %.3f;\n', i, tumors(i).x);
        fprintf(fid2, '        scalar y%d = %.3f;\n', i, tumors(i).y);
    else
        fprintf(fid2, '        scalar raiot%d = 0.00287;\n', i);
        fprintf(fid2, '        scalar ee%d = 0;\n', i);
        fprintf(fid2, '        scalar be%d = raiot%d*pow((1-pow(ee%d,2)),0.25);\n', i, i, i);
        fprintf(fid2, '        scalar ae%d = pow(pow(be%d,2)*(pow(1-pow(ee%d,2),-1)),0.5);\n', i, i, i);
        fprintf(fid2, '        scalar x%d = %.3f;\n', i, tumors(i).x);
        fprintf(fid2, '        scalar y%d = %.3f;\n', i, tumors(i).y);
    end
end
fprintf(fid2, '	       \n');
fprintf(fid2, '        forAll(corr, i)\n');
fprintf(fid2, '        {\n');
fprintf(fid2, '                const scalar x = mesh.C()[i][0];\n');
fprintf(fid2, '                const scalar y = mesh.C()[i][1];\n');
fprintf(fid2, '                const scalar z = mesh.C()[i][2];\n');
for i = 1:num_tumors
    if strcmp(tumors(i).shapeType, 'Circular')
        fprintf(fid2, '                if ( pow(y-y%d,2) <= pow(raiot%d,2) - pow(x-x%d,2) )\n', i, i, i);
    else
        fprintf(fid2, '                if ( pow(y-y%d,2) <= ((1 - pow(x-x%d,2)/pow(ae%d,2) )*pow(be%d,2)) )\n', i, i, i, i);
    end
    fprintf(fid2, '                {\n');
    fprintf(fid2, '                        corr[i] = 1.;\n');
    fprintf(fid2, '                }\n');
end
fprintf(fid2, '        }\n');
fprintf(fid2, '        corr.writeEntry("", os);\n\n');
fprintf(fid2, '        #};\n');
fprintf(fid2, '};\n\n');
fprintf(fid2, 'boundaryField\n{\n');
fprintf(fid2, '    leftWall\n');
fprintf(fid2, '    {\n');
fprintf(fid2, '        type            fixedValue;\n');
fprintf(fid2, '        value           uniform 0;\n');
fprintf(fid2, '    }\n');
fprintf(fid2, '    rightWall\n');
fprintf(fid2, '    {\n');
fprintf(fid2, '        type            fixedValue;\n');
fprintf(fid2, '        value           uniform 0;\n');
fprintf(fid2, '    }\n');
fprintf(fid2, '    lowerWall\n');
fprintf(fid2, '    {\n');
fprintf(fid2, '        type            fixedValue;\n');
fprintf(fid2, '        value           uniform 0;\n');
fprintf(fid2, '    }\n');
fprintf(fid2, '    upperWall\n');
fprintf(fid2, '    {\n');
fprintf(fid2, '        type            fixedValue;\n');
fprintf(fid2, '        value           uniform 0;\n');
fprintf(fid2, '    }\n');
fprintf(fid2, '    defaultFaces\n');
fprintf(fid2, '    {\n');
fprintf(fid2, '        type            empty;\n');
fprintf(fid2, '    }\n');
fprintf(fid2, '}\n\n');
fprintf(fid2, '// ************************************************************************* //\n');

fclose(fid2);
EOF

echo "Conteúdo do script Octave:"
cat $script_octave

echo "Executando Octave"
octave $script_octave

if [ -f "grafico_temperatura.png" ]; then
	echo "Gráfico gerado!"
else
	echo "Erro no gráfico"
fi

rm $script_octave

