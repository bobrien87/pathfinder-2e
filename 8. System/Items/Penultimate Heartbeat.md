---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Spirit]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 2000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This small hunk of slightly rusted iron gives off a faint reddish glow that occasionally pulses when touched. Tales of *penultimate heartbeats* say that the metal attracts a creature's spirit at the moment of death and channels it outward for a grisly display. Once applied to a weapon, a *penultimate heartbeat*'s effects last for 1 hour.

When you reduce a living creature to 0 Hit Points with a weapon under the effect of a *penultimate heartbeat*, it doesn't perish immediately (though is visibly on the brink of death). You can [[Reposition]] the creature up to 10 feet as a free action, after which it dies in a dramatic fashion appropriate to the injury that killed it. Foes in a @Template[type:cone|distance:30] you direct originating from the creature's final position are sprayed with gore, taking @Damage[9d10[spirit]|options:area-damage|traits:emotion,fear,mental] damage from the release of the creature's soul. An affected target attempts a [[Will]] save against your class DC or spell DC, whichever is higher. This effect has the emotion, fear, and mental traits.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Frightened]] 1 from the shock.
- **Failure** The creature takes full damage and is [[Frightened]] 2. For the remainder of the *penultimate heartbeat*'s duration, the creature can't reduce the value of the frightened condition below 1 if it ends its turn where it can see you.
- **Critical Failure** The creature takes double damage and is [[Frightened]] 3. For the remainder of the *penultimate heartbeat*'s duration, the creature can't reduce the value of the frightened condition below 2 if it ends its turn where it can see you.

**Source:** `= this.source` (`= this.source-type`)
