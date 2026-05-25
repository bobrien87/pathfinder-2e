---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 970}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This porous steel coil wraps around a shard of onyx, supplementing the closely guarded science of galvaspheres with the dark magics of unlife. When embedded in a body comprised of flesh, the blood and other fluids catalyze electrical pulses within the coil, activating the necromantic energies. In living creatures, this causes a dangerous surge that can damage the heart. In corpses, however, this can create a limited window of reanimation, with access to the corpse's final memories. Galvanic mortal coils are even rarer than other galvaspheres, and thought by most to be merely hypothetical.

**Activate** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You drive the coil into a living creature that has 0 HP while attaching the other end to yourself, in order to siphon their life force. The galvanic mortal coil increases the target's dying condition by 1. If this kills the target, the coil casts [[False Vitality]] on you.

**Activate** (10 minutes) (manipulate)

**Frequency** once per day

**Effect** You implant the coil into a corpse. The coil casts [[Talking Corpse]] on the body.

**Source:** `= this.source` (`= this.source-type`)
