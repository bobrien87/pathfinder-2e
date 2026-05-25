---
type: creature
group: ["Humanoid", "Xulgath"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Xulgath Skulker"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Xulgath"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Draconic, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +8, Stealth +8, Thievery +8"
abilityMods: ["+3", "+4", "+2", "-1", "+1", "+0"]
abilities_top:
  - name: "Hidden Movement"
    desc: "If a xulgath skulker starts their turn [[Undetected]] by a creature or merely [[Hidden]] from it, that creature is [[Off Guard]] against the skulker's attacks until the end of the skulker's turn."
  - name: "Sneak Attack"
    desc: "A xulgath skulker deals an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +10, **Will** +5"
health:
  - name: HP
    desc: "28"
abilities_mid:
  - name: "Stench"
    desc: "30 feet. DC 16 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+3 slashing"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Mask Stench"
    desc: "`pf2:0` The stalker masks their stench with curated herbs, suppressing their stench aura. The skulker can resume their stench aura as a free action."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Xulgath warrens are patrolled—some might say "haunted"—by the community's skulkers. These xulgaths specialize in stealth, striking swiftly from the shadows and otherwise ambushing foes.

Reptilian humanoids who live in the uppermost reaches of the Darklands, xulgaths (known as troglodytes to many surface-dwelling folk) often attack intruders in their territory on sight. They live in simple familial communities called clutches, battling rival groups and other aggressive Darklands inhabitants in order to survive. They occasionally raid surface settlements, usually at the behest of cruel, bloodthirsty leaders who are often themselves in the thrall of more powerful creatures like nagas or demons. A typical xulgath has dull gray, dark gray, or ashen scales, with a long tail and bony protrusions that run the length of their spine. A typical xulgath is 5 feet tall and weighs 150 pounds.

Although today the xulgaths are brutal and scattered, they were one of the first intelligent humanoids to rise in the primeval world, once ruling over a mighty empire that stretched throughout the Darklands. Today, all that remains of this era are ruins of massive stone ziggurats and crumbling cities found within some of the larger caverns. Some groups of xulgaths continue to live among these ruins, venerating their ancestors' accomplishments, while others consider these areas taboo and leave them to become infested with Darklands vermin. Sages don't agree on why the ancient xulgath civilization fell. Some suspect it was the result of losing several wars waged against serpentfolk, while others suggest that the corruptive influence of demon worship rotted their culture from within.

Certainly, many xulgath settlements continue to worship demons to this day, paying homage and offering live sacrifices to demons or other terrible creatures from the Outer Rifts. Occasionally, a xulgath mystic can call forth and bind a lesser demon to help serve the group, but one who delves too deep into occultism might summon a more powerful fiend that either tears the xulgaths to pieces or seizes control of the settlement.

```statblock
creature: "Xulgath Skulker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
