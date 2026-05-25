---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'gp': 5000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A vaccine grants a creature immunity to a specific strain of disease of a level equal to or less than the vaccine's level, and a +2 item bonus on all saving throws against other strains of the same disease. For example, a vaccine could grant immunity to putrid plague inflicted by harpies, but would only grant a +2 saving throw bonus against putrid plague inflicted by a giant rat.

**Craft Requirements** Creating a vaccine requires a sample of the disease in question.

**Duration** Permanent.

**Special** A vaccine is the same rarity as the disease it's designed to prevent, or as the creature who inflicts the disease if the disease itself doesn't list a rarity.

**Source:** `= this.source` (`= this.source-type`)
