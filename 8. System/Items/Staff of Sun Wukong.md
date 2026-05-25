---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Artifact]]", "[[Divine]]", "[[Monk]]", "[[Parry]]", "[[Reach]]", "[[Trip]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Also known as *Ruyi Bang*, this *+3 major striking greater extending grievous bo staff* is a legendary artifact wielded by the Monkey King, Sun Wukong. Unlike normal bo staves, the *Staff of Sun Wukong* is made of solid iron with two brilliant gold bands at either end.

**Activate—Meteor Slam** `pf2:1` (concentrate, manipulate)

**Frequency** once per day

**Effect** You extend the staff with the force of a meteor, dealing 10d10 bludgeoning damage to a single creature within 120 feet and making it [[Enfeebled]] 1 for 1 day. All other creatures within 10 feet of the target (except the staff's wielder) take @Damage[8d10[sonic]|options:area-damage] damage (DC 43 [[Reflex]] save).

**Activate—Close at Hand** `pf2:f`

**Effect** It's said that Sun Wukong tucked this magical staff behind his ear during his travels. When not in use, the Staff of Sun Wukong shrinks to the size and weight of a needle or toothpick, making it highly concealable (+4 circumstance bonus to Stealth checks to hide it from sight). In this form, the item has negligible Bulk. You can Activate this ability again to return the staff to its normal size.

**Activate—Cloud Somersault** `pf2:1` (manipulate)

**Effect** You use the shapeshifting capabilities of this relic to propel yourself great distances. You [[Leap]] up to 50 feet in any direction.

**Destruction** Despite being made of iron and gold, mundane heat sources can't damage the Staff of Sun Wukong. Magical fire similarly has no effect on this relic. The only way to destroy this item is to expose it to the intense heat of a specific volcano in the depths of the Songil Sea (though which volcano remains shrouded in myth).

**Source:** `= this.source` (`= this.source-type`)
