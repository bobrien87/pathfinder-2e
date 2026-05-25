---
type: creature
group: ["Humanoid", "Kobold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kobold Warrior"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]]"
languages: "Common, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +5, Crafting +2, Stealth +5"
abilityMods: ["+1", "+3", "-1", "+0", "+1", "+1"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The kobold warrior deals an extra 1d4 precision damage to off-guard creatures."
armorclass:
  - name: AC
    desc: "16; **Fort** +3, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "7"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +3 (`pf2:1`), **Damage** 1d6+1 piercing"
  - name: "Melee strike"
    desc: "Spear +5 (`pf2:1`) (thrown 20), **Damage** 1d6+1 piercing"
  - name: "Ranged strike"
    desc: "Sling +5 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Scamper"
    desc: "`pf2:1` **Requirements** The kobold warrior is adjacent to at least one enemy <br>  <br> **Effect** The kobold warrior Strides up to their Speed plus 5 feet and gains a +2 circumstance bonus to AC against reactions triggered by this movement. They must end this movement in a space that's not adjacent to any enemy."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The typical kobold trains in tunnel fighting, learning to use simple weapons that are effective in narrow spaces. Kobolds are capable of landing sneaky strikes against unsuspecting foes, but are just as quick to scamper off to safety when they don't outnumber their enemies by at least two to one.

Kobolds are small reptilian humanoids. They lurk in dark spaces, usually tunnels and mines beneath the earth, in either warrens of their own design or complexes discovered and colonized after the original builders have moved on. Though kobolds are far more pragmatic than courageous, they use every inch of their cunning to even the playing field between themselves and other, stronger creatures. They attack from the darkness and at range, and kobold artificers and engineers master the art of simple but effective traps, which they use to protect their lairs. Kobolds are skilled at working together by necessity, and they often set up ambushes or hit-and-run assaults that allow them to do the most damage possible without being harmed in return.

Kobolds are diligent and hardworking creatures. While some kobolds live in communal collectives that maintain neutral relations with the creatures around them, they can be easily swayed into serving malevolent powers or megalomaniacal leaders. This is in part due to kobolds' innate pragmatism, as they would rather concede to servitude than risk being killed, but it is also in part due to a reverence for the power they generally lack. Notably, kobold eggs left in the proximity of magical creatures or places tend to absorb similar traits from the exposure. The resulting physical changes mark the appearance of each tribe, but a few lucky kobolds are also born with magical power that reflects their tribe's patron.

```statblock
creature: "Kobold Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
