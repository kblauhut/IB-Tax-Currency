package org.ibtc.ibtc;

import java.io.File;
import java.net.URL;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.DragEvent;
import javafx.scene.input.Dragboard;
import javafx.scene.input.MouseEvent;
import javafx.scene.input.TransferMode;
import javafx.scene.layout.Pane;
import javafx.scene.shape.SVGPath;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;

public class PrimaryController {
	File dir;
	
	@FXML
	TextField tfdOutputPath;
	@FXML
	Label tfdFileDropStatus;
	@FXML
	SVGPath svgStatusIcon;
	@FXML
	Pane fileDropField;
	
	@FXML
	public void initialize() {
		fileDropField.setOnDragOver(new EventHandler<DragEvent>() {

            @Override
            public void handle(DragEvent event) {
            	
                if (event.getGestureSource() != fileDropField
                        && event.getDragboard().hasFiles()) {
                    tfdFileDropStatus.setStyle("-fx-text-fill: blue;");
            		svgStatusIcon.setStyle("-fx-text-fill: blue;");
                    event.acceptTransferModes(TransferMode.COPY_OR_MOVE);
                }
                event.consume();
            }
        });

		fileDropField.setOnDragDropped(new EventHandler<DragEvent>() {

            @Override
            public void handle(DragEvent event) {
                Dragboard db = event.getDragboard();
                boolean success = false;
                if (db.hasFiles()) {
                	tfdFileDropStatus.setText(db.getFiles().toString());
                    success = true;
                }
                event.setDropCompleted(success);

                event.consume();
            }
        });
	}
	
	@FXML
	private void btnChooseClicked() {
		Stage stage = new Stage();
		DirectoryChooser directoryChooser = new DirectoryChooser();
		dir = directoryChooser.showDialog(stage);
		if (dir != null) {
			tfdOutputPath.setText(dir.getAbsolutePath());
		}	
	}
}
