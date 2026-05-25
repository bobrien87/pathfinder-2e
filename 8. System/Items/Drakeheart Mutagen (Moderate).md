---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Interact

Your skin grows tough scales like a drake, your eyesight become sharp and your pupils slitted, and your limbs grow wiry and quick, but your mind and reflexes become slow.

**Benefit** You gain +5 item bonus to AC, a Dexterity cap of +2 (as usual, use your lowest Dexterity cap if you have more than one), and a +2 item bonus to Perception checks. If you're wearing armor, you still calculate your proficiency bonus to AC based on your proficiency in the armor you're wearing, even if the drakeheart mutagen has a higher item bonus. You also gain the [[Final Surge]] action.

**Drawback** You take a -1 penalty to Will saves, Reflex saves, and all skill checks to [[Recall Knowledge]].

**Duration** 10 minutes or until you use Final Surge, whichever comes first.

> [!danger] Effect: Drakeheart Mutagen (Moderate)

**Source:** `= this.source` (`= this.source-type`)
