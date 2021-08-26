#include <SPI.h>
//#include <SD.h>
#include "SdFat.h"
SdFat SD;

//CS腳位，預設是SS，以Uno來說就是腳位10，如果有多個SPI設備，請設不同的腳位
#define SD_CS_PIN SS
File myFile;
unsigned long time;
void setup() {
  Serial.begin(9600);
  Serial.print("Initializing SD card...");

  //判斷SD模組初始化是否成功
  if (!SD.begin(SD_CS_PIN)) {
    Serial.println("initialization failed!");
    return;
  }
  Serial.println("initialization done.");

  //打開一個檔名為test.txt的檔案，模式為寫入(FILE_WRITE)
  //若檔案不存在，就會自動建議一個新的檔案
  myFile = SD.open("test.txt", FILE_WRITE);

  // 如果成功打開，就寫入文字
  if (myFile) {
    Serial.print("Writing to test.txt...");
    myFile.println("test");
    // 關閉檔案
    myFile.close();
    Serial.println("done.");
  } else {
    // 如果無法開啟檔案，就在監控視窗顯示訊息
    Serial.println("error opening test.txt");
  }

  //以下是讀取的部份
  //再打開test.txt
    myFile = SD.open("test.txt");
  if (myFile) {
    Serial.println("test.txt:");

    //一直讀取檔案內容，直到沒有為止
    while (myFile.available()) {
      Serial.write(myFile.read()); //把讀到的內容顯示在監控視窗
    }
    // 關閉檔案
    myFile.close();
  } else {
    // 如果無法開啟檔案，就在監控視窗顯示訊息
    Serial.println("error opening test.txt");
  }
}

void loop() {
  time=millis();
  Serial.println(time);
  myFile.println(time);
}
