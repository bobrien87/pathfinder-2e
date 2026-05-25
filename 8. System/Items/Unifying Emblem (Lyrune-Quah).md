---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 60}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These tattoos were first created using designs and techniques from the seven Shoanti clans. Each clan is known for one tattoo in particular. The clans would seal alliances in ancient days by tattooing their emblems on members of other clans to symbolically share their gifts. Though these tattoos are respected, the clans reserve their most prestigious symbols for true members of the clan. The tattoo allows you to understand and speak Shoanti. If you already know that language, you instead gain a +1 item bonus on Diplomacy checks you make when speaking Shoanti to someone who understands it.

The tattoo of the Moon clan depicts the outline of a moon, devoid of any detail.

**Activate** `pf2:2`

**Frequency** once per day

**Effect** The tattoo casts [[Vanishing Tracks]].

**Source:** `= this.source` (`= this.source-type`)
