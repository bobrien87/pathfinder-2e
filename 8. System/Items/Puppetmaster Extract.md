---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 85}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Interact

Distilled from a trighoul's vital fluids, this gummy, ooze-like toxin springs to life when it makes contact with flesh. It swiftly grows spines that dig into the victim, twitching with rudimentary intelligence as they root around for the nervous system. If the toxin embeds itself deeply enough, it seizes control of the victim's body.

Unlike most poisons, puppetmaster extract can affect a dead body with mostly intact flesh. Each round, a corpse without sentience automatically fails its Fortitude save against the poison. At stage 4, the poison stops causing damage and confusion; instead, it reanimates the corpse as an elite [[Plague Zombie]] without the unholy trait; a larger body instead uses statistics for a [[Zombie Brute]] or [[Zombie Hulk]], whichever matches its size. The corpse stands as a free action at the beginning of its turn and attacks nearby creatures. When the poison's duration expires or the poison is cured, the body's state of animation ends.

**Saving Throw** DC 26 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 8 rounds

**Stage 1** 1d12 piercing damage and 1d12 poison damage (1 round)

**Stage 2** 1d12 piercing damage and 2d12 poison (1 round)

**Stage 3** 1d12 piercing damage, 2d12 poison damage, and [[Confused]] for 1 round (1 round)

**Stage 4** 3d12 poison damage and confused for 1 round (1 round)

**Source:** `= this.source` (`= this.source-type`)
