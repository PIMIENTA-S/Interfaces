package com.example.demo;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class actividad_1 extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Label texto = new Label("Bienvenido esta es la primer Scene");

        Button boton = new Button("ir a la scene 2");

        boton.setOnAction(actionEvent -> nuevaVentana());

        VBox vBox = new VBox(20);
        vBox.getChildren().addAll(texto, boton);

        Scene scene = new Scene(vBox, 300, 200);

        stage.setScene(scene);
        stage.setTitle("Titulo");
        stage.show();


    }

    private void nuevaVentana(){

        Stage ventana1 = new Stage();
        ventana1.setTitle("Titulo");

        
        Button boton1 = new Button("Volvamos a el primer Stage");

        BorderPane root = new BorderPane();
        
        root.setCenter(boton1);
        
        boton1.setOnAction(actionEvent -> ventana1.close());
        

        Scene scene1 = new Scene(root, 500, 300);
        ventana1.setScene(scene1);
        ventana1.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}