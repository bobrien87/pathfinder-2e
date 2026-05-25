---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]", "[[Noisy]]"]
price: "{'gp': 6500}"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater resilient greater electricity-resistant chain mail* is adorned with two golden thunderbolts, one along each forearm. Even on a seemingly cloudless day, you can raise your arms to the heavens and draw down a bolt of lightning upon yourself, empowering your armor and blasting your enemies.

**Activate—Call Down Lightning** `pf2:1` (concentrate, electricity, manipulate)

**Frequency** once per day

**Effect** You conjure a bolt of electricity down onto yourself, dealing @Damage[6d6[electricity]|options:area-damage|traits:concentrate,electricity,manipulate] damage to all creatures in a @Template[type:emanation|distance:10]. Additionally, for the next minute, whenever a creature touches you or hits you with a melee unarmed attack or a non-reach melee weapon attack, it takes @Damage[1d8[electricity]|traits:concentrate,electricity,manipulate] damage.

**Source:** `= this.source` (`= this.source-type`)
