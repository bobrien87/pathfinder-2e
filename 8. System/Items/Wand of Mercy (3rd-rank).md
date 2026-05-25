---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 425}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The pommel of this rose quartz wand resembles the stylized wings of an angel. When you cast its spell and choose not to make it nonlethal, the crystal deepens to blood red. The color reverts to rose when you cast the spell from the wand nonlethally.

**Activate** Cast a Spell; the activation takes `pf2:2` if the spell normally takes `pf2:1` to cast, or `pf2:3` if the spell normally takes `pf2:2`

**Frequency** once per day, plus overcharge

**Effect** You Cast the Spell, and can choose to give it the nonlethal trait.

**Craft Requirements** Supply a casting of a spell of the appropriate rank. The spell must have a casting time of `pf2:1` or `pf2:2`, it must deal damage, and it can't have the death, void, or nonlethal traits.

**Source:** `= this.source` (`= this.source-type`)
