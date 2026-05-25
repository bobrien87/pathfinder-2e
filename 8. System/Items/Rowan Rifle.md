---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Backstabber]]", "[[Concussive]]", "[[Fatal d12]]", "[[Primal]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

In a dense forest within Arcadia, djezet fell from the sky millennia ago, even before Earthfall. While this metal was poisonous to most of the plant life growing nearby, one stubborn rowan tree refused to die, its roots slowly absorbing djezet in small particles from the ground until the entire plant was suffused with it. Fey bowyers discovered the remarkable plant and coaxed it into growing into a very particular shape, its branching trunks woven together into a tightly twisted and naturally rifled barrel.

These legendary starmetal weapons are Arcadia's greatest treasures. The *Rowan Rifle* star gun is a *+2 greater fearsome quickstrike greater striking* advanced firearm with a range of increment of 300 feet. It deals 1d8 fire damage and has the backstabber, concussive, and fatal d12 traits.

As a star gun, the *Rowan Rifle* runs on magic, and doesn't use ammunition or black powder. As a weapon forged to protect the fey peoples of Arcadia, the *Rowan Rifle*'s enchantments prevent it from ever causing harm to a creature with the fey trait; any attempt to shoot a fey with it results in an automatic misfire. This legendary star gun is as much a badge of office as a weapon, as it denotes dominion over all Briarbough. If the *Rowan Rifle*'s wielder is fey, or if they were specifically given the *Rowan Rifle* by a fey creature who recognized them as a worthy champion, they can use the following activations.

**Activate—Season's Cycle** `pf2:1` (concentrate)

**Effect** You will the *Rowan Rifle* to change the energy it fires from the white-hot energy of summer that glows like a star to the shivering chill of winter, the crackling electricity of the storm, or even the sonic vibrations of a roar. The *Rowan Rifle*'s damage type changes from its current damage type to cold, electricity, fire, or sonic. On the next sunrise, the *Rowan Rifle* returns to dealing fire damage.

**Activate—Skymetal Shot** `pf2:2` (manipulate)

**Effect** The *Rowan Rifle* fires a @Template[type:line|distance:60] of liquid djezet that wraps around all creatures in the affected area before hardening, which impedes them with metallic vines unless the affected creature succeeds at a [[Reflex]] save. A creature who fails the save takes a –15-foot circumstance penalty to their Speeds, and a creature who critically fails is [[Immobilized]]. A creature who succeeds at a `act escape show-dc=all dc=35` check ends this effect. Otherwise, the djezet vines last for 10 minutes before crumbling away.

**Activate—Briarbough Brachiaport** 1 minute (concentrate, manipulate)

**Frequency** once per 10 minutes

**Effect** You hold aloft the *Rowan Rifle* and step into a tree in Briarbough, and you use [[Nature's Pathway]] to travel to another tree in Briarbough.

**Source:** `= this.source` (`= this.source-type`)
