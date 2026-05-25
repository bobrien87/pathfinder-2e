---
type: creature
group: ["Fetchling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fetchling Scout"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fetchling"
trait_02: "Humanoid"
trait_03: "Shadow"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common, Shadowtongue"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +4, Deception +5, Diplomacy +5, Society +3, Stealth +7, Thievery +7"
abilityMods: ["+1", "+4", "+2", "+0", "+0", "+2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The fetchling scout's Strikes deal an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Shadow Blending"
    desc: "When the fetchling scout is [[Concealed]] as a result of dim light, the flat check to target them has a DC of 7, not 5."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+1 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 15, attack +7<br>**1st** [[Illusory Disguise]]"
abilities_bot:
  - name: "Shadow Stride"
    desc: "`pf2:1` **Requirements** The fetchling is in dim light <br>  <br> **Effect** The fetchling Strides. They have a +10-foot status bonus to their Speed during this Stride. The DC from shadow blending increases to DC 11 flat check during this Stride, and the fetchling remains [[Concealed]] by dim light until the end of the movement, even if they leave dim light during the Stride."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fetchling scouts patrol the outskirts of their communities, looking for any possible threats.

The people known today as fetchlings are a distinct ancestry descended from generations of humans who became trapped ages ago on the Netherworld. No longer human at all, these people, who call themselves kayals, have become monochromatic in coloration, with flesh tones and hair colors varying between white, black, and all shades of gray. Their limbs are lithe and willowy, and their eyes are generally solid yellow, yellow-green, or white, though a rare few have a purple or blue glow.

Fetchlings have developed their own complex societies in the Netherworld, often under the tolerance of or in servitude to the strange, malignant creatures there, such as sinister velstracs or enigmatic d'ziriaks. While individual fetchlings have their own morals and codes, they are all survivors in a harsh environment, which leads to a tendency toward pragmatism. Fetchling clothing mimics the regions they dwell in, with drab colors tending toward darker shades. When they trade with humans or other societies in the Universe, they often wear masks or concealing clothing to hide their appearance.

Typical fetchling communities are insular and swiftly close ranks in the event of an intruder. Though individual fetchlings don't mind traveling to and blending in with other societies to facilitate trade, they often hide or even react defensively if they have their own visitors. When one considers the nature of the other denizens of the Netherworld, however, this tendency to assume the worst of interlopers might make sense. Fetchling communities in the Universe are rare, but do exist in small pockets. These communities tend to be somewhat more open than those in the Netherworld. Many fetchling adventurers originate from these enclaves, as the curiosity to see the world beyond the shadows is often a difficult one to sate.

```statblock
creature: "Fetchling Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
