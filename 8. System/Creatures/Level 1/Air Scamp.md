---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Air Scamp"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +7, Stealth +7"
abilityMods: ["+1", "+4", "+0", "-2", "+0", "+0"]
abilities_top:
  - name: "Fog Vision"
    desc: "The air scamp ignores the [[Concealed]] condition from fog and mist."
armorclass:
  - name: AC
    desc: "16; **Fort** +3, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "12; fast healing 2 (in open air); **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Fast Healing 2 (In Open Air)"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+1 piercing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17, attack +9<br>**2nd** [[Blur]]<br>**1st** [[Gust of Wind]]"
abilities_bot:
  - name: "Sirocco Breath"
    desc: "`pf2:2` The air scamp creates cutting winds in a @Template[cone|distance:15] that deal @Damage[2d6[slashing]|options:area-damage] damage to each creature within the area (DC 17 [[Reflex]] save). A creature that fails its save is also pushed back 10 feet. <br>  <br> The air scamp can't use Sirocco Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A pale blue head and paper-thin wings peek out from the cloud that clings to the air scamp. Air scamps are short-sighted and flighty, even relative to their kin; they are as likely to fly recklessly into battle as they are to whine in terror at a loud noise.

Elemental scamps are bat-like critters marked by elemental powers. Scamps are dispatched from the Elemental Planes by more powerful residents or called to the Universe by neophyte summoners. All scamps have a hint of magical power due to a lingering connection to their home plane, which they largely use to pull simple pranks.

Scamps rapidly form a pecking order of cleverness. Humanoids often confuse scamps when meeting such creatures for the first time. These confused scamps usually resort to an escalating series of pranks and mischief, seeing what they can get away with to establish their place in the hierarchy.

```statblock
creature: "Air Scamp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
