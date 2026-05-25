---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Incorporeal]]", "[[Magical]]"]
price: "{'gp': 160}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This otherworldly prosthetic arm is the product of psychopomp magic. An *aether appendage* is incorporeal so long as no item is being held in the hand or worn on the arm.

**Activate** `pf2:1` (concentrate)

You cause the arm to become corporeal until the end of your turn, allowing you to use it to make Strikes or grasp objects. It remains corporeal if you're holding an item or it's wearing an item at the end of your turn. Your unarmed attack Strikes made with the *aether appendage* are magical. If they're already magical, they instead gain the effect of the ghost touch property rune.

**Activate** `pf2:1` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You're holding a non-magical item of light or negligible Bulk

**Effect** The item becomes incorporeal for 1 minute. Your *aether appendage* can use the incorporeal item normally.

**Source:** `= this.source` (`= this.source-type`)
