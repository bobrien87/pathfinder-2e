---
type: creature
group: ["Amphibious", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Water Scamp"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Amphibious"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +6, Stealth +6"
abilityMods: ["+1", "+3", "+1", "-2", "+0", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +11, **Will** +4"
health:
  - name: HP
    desc: "20; fast healing 2 (while underwater); **Immunities** bleed, paralyzed, poison, sleep; **Resistances** acid 3, fire 3"
abilities_mid:
  - name: "Fast Healing 2 (While Underwater)"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +8 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d6+1 slashing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17, attack +9<br>**2nd** [[Acid Grip]]<br>**1st** [[Create Water]]"
abilities_bot:
  - name: "Acid Breath"
    desc: "`pf2:2` The water scamp breathes acid in a @Template[cone|distance:15] that deals @Damage[2d6[acid]|options:area-damage] damage to each creature within the area (DC 17 [[Reflex]] save). <br>  <br> The water scamp can't use Acid Breath again for 1d4 rounds."
  - name: "Drench"
    desc: "`pf2:1` The water scamp shakes out a seemingly endless supply of water from its fur to put out all fires in a @Template[emanation|distance:5]. The scamp extinguishes all non-magical fires automatically and attempts to counteract magical fires (+7 counteract modifier)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Water scamps are marked apart from other scamps by sleek fur that traps a layer of water next to their skin. Although they can fly like their kin and conjure enough water to never dry out, water scamps leave the water only when they must. Although air-breathing scholars consider these scamps quiet and rather skittish, underwater civilizations find their exuberance and playfulness can be overwhelming.

Elemental scamps are bat-like critters marked by elemental powers. Scamps are dispatched from the Elemental Planes by more powerful residents or called to the Universe by neophyte summoners. All scamps have a hint of magical power due to a lingering connection to their home plane, which they largely use to pull simple pranks.

Scamps rapidly form a pecking order of cleverness. Humanoids often confuse scamps when meeting such creatures for the first time. These confused scamps usually resort to an escalating series of pranks and mischief, seeing what they can get away with to establish their place in the hierarchy.

```statblock
creature: "Water Scamp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
