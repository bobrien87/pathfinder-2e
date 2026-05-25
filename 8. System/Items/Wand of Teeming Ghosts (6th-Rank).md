---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 4500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This pale wooden wand is carved to resemble a thigh bone with metal caps at each end. Ghostly tendrils seem to swirl around it every so often.

**Activate** [[Cast a Spell]]

**Frequency** once per day, plus overcharge

**Effect** You cast [[False Vitality]] at 6th-rank. During the duration of the spell, wisps that resemble spirits flit around you as long as you have any temporary Hit Points from *false vitality*, and you can use the following action.

**Activation** `pf2:f` (concentrate)

**Trigger** You successfully impart the [[Frightened]] 1 condition to a creature

**Requirements** You have at least 1 temporary Hit Point from *false vitality*

**Effect** You end *false vitality* and increase the creature's frightened condition value to 2.

**Craft Requirements** Supply a casting of *false vitality* at 6th-rank

**Source:** `= this.source` (`= this.source-type`)
