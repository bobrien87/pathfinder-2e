---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Melody on the Wind"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +22, Athletics +19, Performance +22, Stealth +22"
abilityMods: ["+4", "+6", "+2", "+2", "+5", "+6"]
abilities_top:
  - name: "Swiftness"
    desc: "The melody on the wind's movement doesn't trigger reactions."
armorclass:
  - name: AC
    desc: "30; **Fort** +16, **Ref** +22, **Will** +19"
health:
  - name: HP
    desc: "170; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Hostile Duet"
    desc: "`pf2:r` **Trigger** A hostile creature within 30 feet creates an effect with the auditory trait that provides bonuses to itself or its allies <br>  <br> **Effect** The melody on the wind recreates the effect, gaining the bonuses for itself and its allies as long as the original effect persists."
  - name: "Retune"
    desc: "`pf2:r` **Trigger** The melody on the wind is targeted by a spell that has the auditory trait <br>  <br> **Effect** The melody on the wind attempts to counteract the spell with a Performance check. If it succeeds, the spell effect is caught in a blast of wind that sweeps it back to its origin, affecting the caster. Targets of the triggering effect other than the melody on the wind are still affected normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wind Gust +23 (`pf2:1`) (agile, finesse), **Damage** 2d10+10 bludgeoning plus [[Push]]"
  - name: "Ranged strike"
    desc: "Solid Refrain +23 (`pf2:1`) (range 70 ft.), **Damage** 2d8+10 sonic"
spellcasting: []
abilities_bot:
  - name: "Mesmerizing Melody"
    desc: "`pf2:1` The melody on the wind sings in a sonorous chorus. Any creature in a @Template[type:emanation|distance:30] must attempt a DC 29 [[Will]] save to resist becoming [[Fascinated]] by the melody on the wind. A creature that succeeds at its save is temporarily immune for 24 hours. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is fascinated by the melody on the wind for 1 round. <br> - **Failure** The creature is fascinated by the melody on the wind for 4 rounds."
  - name: "Push"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

While the melody on the wind, known by some as a song elemental, might enjoy the beauty of music, it is by nature a destructive elemental force.

Some elementals embody aspects of air, such as smoke, lightning, and fog.

```statblock
creature: "Melody on the Wind"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
