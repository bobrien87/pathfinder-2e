---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 17}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

The shaft of this arrow is covered in fine green scales, and its iron head comes to a pair of points almost like fangs.

After an activated viper arrow hits a target, the arrow transforms into a [[Viper]]. The target is affected by the viper's poison, as if it had been bitten. The viper then lands in an open space adjacent to the target.

The viper has the summoned trait and acts at the end of your turn, even though you didn't use the Sustain a Spell action. It is under the GM's control, but it generally attacks the creature the arrow struck. The viper vanishes after 1 minute or when slain.

**Craft Requirements** Supply one casting of [[Summon Animal]]

**Source:** `= this.source` (`= this.source-type`)
