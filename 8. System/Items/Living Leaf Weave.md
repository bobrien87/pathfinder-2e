---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Healing]]", "[[Laminar]]", "[[Plant]]"]
price: "{'gp': 160}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of leaf weave armor is specially modified to metabolize the alchemical accelerants in medicinal compounds. A special receptacle in the armor can hold an Elixir of Life, which takes 3 Interact actions to install.

**Activate** `pf2:1` (manipulate)

**Requirements** An elixir of life is installed in the armor

**Effect** Slithering vines grow from the armor, granting an item bonus to Athletics checks to [[Grapple]], to your Fortitude DC to resist Grapple, [[Disarm]], or [[Shove]] attempts, and to your Reflex DC to resist [[Trip]] attempts. The bonus is equal to the elixir's item bonus, and lasts for 3 rounds. The activation uses up the elixir, and the armor can't be activated again until a new one is installed.

**Source:** `= this.source` (`= this.source-type`)
