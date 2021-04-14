# 디스코드 봇 바롬

const Discord = require('discord.js');
const client = new Discord.Client();
const token = '//여기에 토큰';

client.on('ready', () => {
    console.log('hello!');
});

client.on('message', (message) => {
    if(message.content ==='#원하는 욕') {
        message.reply('#욕을 인식했을때 대답 할 말')
    }
});

client.on('message', async message => {

    let blacklisted = ["ㅅㅂ", "ㅅ@ㅂ", "tlqkf", "fuck", "진지충", "급식충", "틀딱", "시발", "개소리", "지랄", "잼민이",
    "ㄳㄲ", "미친놈","ㅁㅊㄴ", "존나", "ㅈㄴ","느금", "고자", "걸레", "김치녀", "개초딩", "꼰대", "노답", "나가뒤져", 
    "나가죽어", "닥쳐", "닭대가리", "돌대가리", "새대가리", "등신", "병신", "따까리", "땡중", "떨거지", "또라이", "돌아이", "똘마니", "띨빵", "망나니",
    "맘충", "머저리", "무뇌", "미친년", "미친놈", "바보멍청이해삼멍게말미잘", "병신따까리", "빨갱이", "뻐큐", "빡대가리", "사이코", "십장생", "쌍놈", "쌍년", "썅", "씹쓰레기", 
    "씹지랄", "씹창", "아가리", "아다", "애새끼", "애새", "애자", "양놈", "양키", "앰흑", "엠창", "니미씨발", "엄창", "염병", "옘병", "왕따", 
    "왜놈", "찐따", "좆", "좆까", "좆밥", "짱깨", "장궤", "쪼다쪽발이", "쪽바리", "쫄보", "찐찌버거", "찐따", "찌질이", "버러지", "창녀", "창놈", "추남", "추녀", "틀딱충" ,
    "후빨", "흑형", "사가지", "싸가지", "놈", "년", "충","새끼", "ㅅㄲ", "toRL", "좃"]

    let foundInText = false;
    for (var i in blacklisted) { 
      if (message.content.toLowerCase().includes(blacklisted[i].toLowerCase())) foundInText = true
    }

    if (foundInText) {
        const user = message.author.id;
        const embed = new Discord.MessageEmbed()
        .setColor('#FF0000')
        .setDescription('<@${user}> #위에있는 욕이 인식되었을때 대답 말');
  
        message.channel.send(embed)
}
}
);

client.login(token);
