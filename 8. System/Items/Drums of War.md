---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 90}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This handheld snare drum is adorned with garish scenes of battle and triumph. When played, no matter what rhythm, it always gives the impression of a marching beat, invoking armies on the move. While playing the drums, you gain a +1 item bonus to Performance checks and a +5-foot status bonus to your Speed.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** [[Shield]]
- **1st** [[Force Barrage]], [[Mystic Armor]], [[Sure Strike]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
