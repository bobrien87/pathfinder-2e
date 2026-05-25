---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Earth Scamp"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +6, Stealth +2"
abilityMods: ["+3", "-1", "+2", "-2", "+0", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +4, **Will** +3"
health:
  - name: HP
    desc: "20; fast healing 2 (while underground); **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Fast Healing 2 (While Underground)"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Body +8 (`pf2:1`), **Damage** 1d6+3 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17, attack +9<br>**3rd** [[One with Stone]]<br>**2nd** [[Enlarge (Self Only)]]"
abilities_bot:
  - name: "Scree Breath"
    desc: "`pf2:2` The earth scamp breathes rocks in a @Template[cone|distance:15] that deals @Damage[2d6[bludgeoning]|options:area-damage] damage to each creature within the area (DC 17 [[Reflex]] save). <br>  <br> The earth scamp can't use Scree Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

An earth scamp's rocky exterior could camouflage it well among loose rocks if not for the scamp's large eyes and bat-like wings. Earth scamps can fly, but the act of flight is uncomfortable and unnerving to them—they rarely leave the ground if they can help it. In fact, most earth scamps would rather never visit the surface at all, staying nestled deeply within the rocks they resemble.

Elemental scamps are bat-like critters marked by elemental powers. Scamps are dispatched from the Elemental Planes by more powerful residents or called to the Universe by neophyte summoners. All scamps have a hint of magical power due to a lingering connection to their home plane, which they largely use to pull simple pranks.

Scamps rapidly form a pecking order of cleverness. Humanoids often confuse scamps when meeting such creatures for the first time. These confused scamps usually resort to an escalating series of pranks and mischief, seeing what they can get away with to establish their place in the hierarchy.

```statblock
creature: "Earth Scamp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
