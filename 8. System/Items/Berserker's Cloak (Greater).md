---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Invested]]", "[[Primal]]"]
price: "{'gp': 40000}"
usage: "worncloak"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bearskin includes the head and bared teeth of the mighty creature from which it was taken. When worn, the cloak drapes over your head and around your shoulders, imbuing you with a bear's ferocity.

If you have the [[Rage]] action, while raging you grow jaws that deal 1d10 piercing damage and claws that deal 1d6 slashing damage and have the agile trait. This transformation is a morph effect, and both the jaws and claws are unarmed attacks in the brawling weapon group. You gain the benefits of a *+2 weapon potency* rune and a greater *striking* rune with these attacks (gaining a +2 item bonus to attack rolls and increasing the weapon damage dice by two).

If you have an animal instinct and the bestial rage instinct ability, instead of gaining these unarmed attacks, your unarmed attacks from the bestial rage instinct ability gain the benefits of a *+3 weapon potency* rune and a *major striking* rune (granting a +3 item bonus to attack rolls and increasing the weapon damage dice by three).

**Source:** `= this.source` (`= this.source-type`)
