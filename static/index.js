const player_data_element = document.getElementById("player_data");

window.onload = async () => {
    const request = await fetch("/api/data");
    const player_array = await request.json();

    if (player_array.length <= 0) {
        player_data_element.innerHTML = `
            <h2>No player entries.</h2>
        `;
        
        return;
    }
    
    // player_array format: Player[], Player: {bounty: number, tokens: number, username: string, uuid: string}
    for (let i = 0; i < player_array.length; i++) {
        const player = player_array[i];
        player_data_element.innerHTML += `
            <div class="player" id="${player.uuid}">
                <img alt="Player Head" src="https://mc-heads.net/avatar/${player.uuid}" class="player_head" />
                <h2>${player.username}</h2>
                <section class="stat">
                    <img alt="Money" src="/static/money.svg" class="money" />
                    <span>${player.tokens}</span>
                </section>
                <section class="stat">
                    <img alt="Bounty" src="/static/bounty.svg" class="bounty" />
                    <span>${player.bounty}</span>
                </section>
            </div>
        `;
    }
}