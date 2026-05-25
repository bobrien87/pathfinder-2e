---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 33}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Rows of triangles symbolizing shark teeth protect you from danger and enable you to take fierce retaliation against those who try to harm you. Seafarers, especially those on the seas of Minata, wear these tattoos in patterns, with multiple rows of regular triangles. You gain a +1 item bonus to Survival checks to navigate bodies of water.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You would be hit by an attack against your AC

**Effect** You gain a +1 circumstance bonus to AC against the attack, or a +2 circumstance bonus if the attacker is in water or has the amphibious, aquatic, or water trait. Whether the attack hits or misses, you gain a +2 status bonus to damage with the next Strike you make against the attacker before the end of your next turn.

> [!danger] Effect: Triangular Teeth

**Source:** `= this.source` (`= this.source-type`)
