---
type: creature
group: ["Construct", "Devil"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Levaloch"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Devil"
trait_03: "Fiend"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Greater Darkvision]]"
languages: "Diabolic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +17, Intimidation +14, Religion +14"
abilityMods: ["+6", "+3", "+4", "+2", "+3", "+1"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Hellstrider"
    desc: "A levaloch ignores the effects of non-magical difficult terrain. They take no damage from caltrops or from damaging terrain that deals physical, acid, or cold damage. <br>  <br> A levaloch can move through liquids up to 5 feet deep at their full Speed."
  - name: "Barbed Net"
    desc: "When a levaloch hits a creature with their barbed net, the net wraps around the target, which becomes [[Clumsy]] 1 and takes a -10-foot circumstance penalty to its Speeds. If the Strike was a critical success, the target is also [[Immobilized]]. <br>  <br> When a creature Escapes, or if the Strike misses, the net crumbles into rust. <br>  <br> Each time a creature attempts to Escape, it takes 1d6 slashing damage from the net's barbs, regardless of whether the attempt succeeds. <br>  <br> > [!danger] Effect: Barbed Net"
  - name: "Merciless Thrust"
    desc: "When a levaloch hits a creature that has the [[Clumsy]], [[Enfeebled]], [[Immobilized]], or [[Restrained]] conditions with a melee trident Strike, the Strike deals an additional 2d6 damage."
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "105; **Immunities** fire; **Weaknesses** holy 5; **Resistances** physical 5 except silver"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Phalanx Fighter"
    desc: "All devils of equal or lower level adjacent to a levaloch gain a +1 circumstance bonus to their AC as the levaloch shields them from harm. <br>  <br> > [!danger] Effect: Phalanx Fighter"
  - name: "Stable Stance"
    desc: "A levaloch gains a +2 circumstance bonus to their Fortitude DC against being Shoved and to other saving throws to resist being moved against their will."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +19 (`pf2:1`) (magical, unholy), **Damage** 2d8+12 piercing plus [[Merciless Thrust]]"
  - name: "Melee strike"
    desc: "Trident +16 (`pf2:1`) (magical, thrown 20, unholy), **Damage** 2d8+12 piercing"
  - name: "Ranged strike"
    desc: "Barbed Net +16 (`pf2:1`) (magical, unholy, range 20 ft.), **Damage**  plus [[Barbed Net]]"
spellcasting: []
abilities_bot:
  - name: "Forge Weapon"
    desc: "`pf2:1` A levaloch reforges part of their barbed iron substance into a new *+1 [[Striking]] trident* or barbed net. Their previous trident crumbles to rust. <br>  <br> When the levaloch is destroyed, any tridents or barbed nets they created crumble to rust."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fearsome giants of jagged iron, levalochs serve in the armies of Hell as potent warriors and tenacious hunters-creatures of absolute discipline endlessly obedient to diabolical tyrants.

There are countless legions of lawful fiends in the nine layers of Hell, warring against the celestial planes and scouring the Material Plane for souls to corrupt.

```statblock
creature: "Levaloch"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
