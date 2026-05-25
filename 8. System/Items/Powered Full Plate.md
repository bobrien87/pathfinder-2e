---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Bulwark]]"]
price: "{'gp': 360}"
bulk: "4"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Stasian actuators help the limbs of this full plate move of their own accord, as long as they're supplied with power. A chamber in the chest plate can hold a single Bottled Lightning, which takes 3 Interact actions to install.

**Activate** `pf2:1` (manipulate)

**Requirements** A bottled lightning is installed in the armor

**Effect** The armor powers up for 10 minutes. While it's powered up, add the bottled lightning's item bonus to your Athletics checks to [[Force Open]], [[High Jump]], [[Long Jump]], and [[Shove]]. The armor's Strength requirement is lowered by 1, or by 2 if the loaded bottled lightning's item bonus to attack rolls is +3 or higher. The armor's normal penalties still apply, based on this altered Strength. The activation uses up the bottled lightning, and the armor can't be activated again until a new one is installed.

**Source:** `= this.source` (`= this.source-type`)
