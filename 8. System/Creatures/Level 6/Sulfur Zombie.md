---
type: creature
group: ["Fire", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sulfur Zombie"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fire"
trait_02: "Mindless"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: "Zombie"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +12"
abilityMods: ["+5", "+2", "+4", "-5", "+2", "-2"]
abilities_top:
  - name: "Slow"
    desc: "A sulfur zombie is permanently [[Slowed]] 1 and can't use reactions."
  - name: "Blinding Sulfur"
    desc: "A sulfur zombie burns with putrid inner fire. A creature hit by a sulfur zombie's fist Strike must attempt a DC 22 [[Fortitude]] save. On a failure, the creature is [[Blinded]] for 1 round, or for 1 minute on a critical failure."
armorclass:
  - name: AC
    desc: "23; **Fort** +16, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "125; void healing; **Immunities** bleed, death effects, disease, fire, mental, paralyzed, poison, unconscious; **Weaknesses** slashing 7, vitality 7"
abilities_mid:
  - name: "Death Throes"
    desc: "When a sulfur zombie dies, its body explodes in a @Template[type:burst|distance:30] of fire and debris that deals @Damage[2d10[bludgeoning],2d10[fire]|options:area-damage]{2d10 bludgeoning damage and 2d10 fire damage} to each creature in the area (DC 21 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`), **Damage** 2d6+5 bludgeoning plus 1d6 fire plus [[Blinding Sulfur]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Glowing with a dull amber light, these odious creatures spawn from a combination of baleful magic and fire. These destructive creations sow chaos and demolish fortifications, making them the bane of besieged cities.

Necromancers most often create these mindless undead as obedient, expendable servitors. Left to its own devices, a zombie seeks only to consume the living, stopping only when its rotting body can no longer hold together.

```statblock
creature: "Sulfur Zombie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
