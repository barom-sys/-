# -디스코드 봇 바롬

const Discord = require('discord.js');
const client = new Discord.Client();
const token = '//여기에 토큰';

client.on('ready', () => {
    console.log('hello!');
});

client.on('message', (message) => {
    if(message.content ==='도움말') {
        message.reply('안녕하세요. 저희는 운산고등학교 INPRO 입니다. 바롬의 메인개발자는 K입니다. 요류 발생시 연락주세요.')
    }
});

client.on('message', (message) => {
    if(message.content ==='운산고등학교') {
        message.reply('자랑스러운 운산고등학교 http://www.woonsan.hs.kr/wah/main/index.htm`')
    }
});

client.on('message', (message) => {
    if(message.content ==='존나') {
        message.reply('학생들이 자주쓰는 존나는 남성의 성기를 비하하는 말인 좃 에서 파생된 말입니다. ')
    }
});

client.on('message', (message) => {
    if(message.content ==='ㅈㄴ') {
        message.reply('학생들이 자주쓰는 존나는 남성의 성기를 비하하는 말인 좃 에서 파생된 말입니다.')
    }
});

client.on('message', (message) => {
    if(message.content ==='좃까') {
        message.reply('남자의 성기를 까라는 말 입니다. 욕을 줄입시다')
    }
});

client.on('message', (message) => {
    if(message.content ==='ㅈㄲ') {
        message.reply('남자의 성기를 까라는 말 입니다. 욕을 줄입시다')
    }
});

client.on('message', (message) => {
    if(message.content ==='tlqkf') {
        message.reply('영어로 쳐도 욕은 욕입니다. 씨발의 뜻은 성관계 이므로 욕을 줄입시다.')
    }
});

client.on('message', (message) => {
    if(message.content ==='병신') {
        message.reply('병신은 장애인을 일컫는 말 입니다. 인터넷 에서 욕을 잘 쓰지 않도록 노력 합시다.')
    }
});

client.on('message', (message) => {
    if(message.content ==='새끼') {
        message.reply('새끼는 본래 시아우를 가리키던 시아기 에서 유래 되었습니다 하지만 오늘날 새끼는 어린것, 놈 이라는 단어로 쓰이고 있습니다. ')
    }
});

client.on('message', (message) => {
    if(message.content ==='씨발') {
        message.reply('씨발 이라는 뜻은 성관계라는 뜻 입니다. 욕을 줄입시다. ')
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
        .setDescription('<@${user}> !경고! 욕을 사용하는 모습은 보기 안 좋습니다. 욕을 줄이기 위해 상담을 원하신다면 이 링크를 타고 들어가세요! https://www.cyber1388.kr:447/ ');
  
        message.channel.send(embed)
}
}
);

client.login(token);
