---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]", "[[Polymorph]]", "[[Wand]]"]
price: "{'gp': 55000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The grain of this simple wooden wand forms shifting images of sharp claws, snapping jaws, and countless creatures.

**Activate** Cast a Spell; This activation takes `pf2:2` if the spell normally takes `pf2:1` to cast, or `pf2:3` if the spell normally takes `pf2:2`

**Frequency** once per day, plus overcharge

**Effect** You Cast the Spell, selecting two forms from among those you can normally choose. You gain the benefits of both forms. For example, if one form can breathe air and the other can breathe underwater, you can breathe in both situations. If there's overlap in abilities, you gain the better one. For instance, if both have a fly Speed, you get the higher one, and if both forms have claws, you gain only the claw Strike you prefer. The GM determines which abilities overlap and which are cumulative.

**Craft Requirements** Supply a casting of a spell of the appropriate rank. The spell must have a casting time of `pf2:1` or `pf2:2`, must have the polymorph trait, and must allow more than one choice of battle form.

**Source:** `= this.source` (`= this.source-type`)
