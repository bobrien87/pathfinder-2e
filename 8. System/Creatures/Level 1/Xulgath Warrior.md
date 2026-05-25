---
type: creature
group: ["Humanoid", "Xulgath"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Xulgath Warrior"
level: "1"
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
    desc: "+6; [[Darkvision]]"
languages: "Draconic, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +7, Stealth +5"
abilityMods: ["+4", "+2", "+3", "-1", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +8, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "21"
abilities_mid:
  - name: "Stench"
    desc: "30 feet. DC 16 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +9 (`pf2:1`), **Damage** 1d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (agile, unarmed), **Damage** 1d4+4 slashing"
  - name: "Melee strike"
    desc: "Club +7 (`pf2:1`) (thrown 10), **Damage** 1d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +7 (`pf2:1`) (thrown 30), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Xulgath warriors strike with fury and eager cruelty, always ready for the next fight. The taking of prizes from battle—including weapons and items stolen from defeated foes along with grislier trophies harvested from fallen victims' flesh—is a popular pursuit among these vicious reptiles, and those whose armor and scales are most adorned are awarded the greatest respect (and perhaps fear) from their kin.

Reptilian humanoids who live in the uppermost reaches of the Darklands, xulgaths (known as troglodytes to many surface-dwelling folk) often attack intruders in their territory on sight. They live in simple familial communities called clutches, battling rival groups and other aggressive Darklands inhabitants in order to survive. They occasionally raid surface settlements, usually at the behest of cruel, bloodthirsty leaders who are often themselves in the thrall of more powerful creatures like nagas or demons. A typical xulgath has dull gray, dark gray, or ashen scales, with a long tail and bony protrusions that run the length of their spine. A typical xulgath is 5 feet tall and weighs 150 pounds.

Although today the xulgaths are brutal and scattered, they were one of the first intelligent humanoids to rise in the primeval world, once ruling over a mighty empire that stretched throughout the Darklands. Today, all that remains of this era are ruins of massive stone ziggurats and crumbling cities found within some of the larger caverns. Some groups of xulgaths continue to live among these ruins, venerating their ancestors' accomplishments, while others consider these areas taboo and leave them to become infested with Darklands vermin. Sages don't agree on why the ancient xulgath civilization fell. Some suspect it was the result of losing several wars waged against serpentfolk, while others suggest that the corruptive influence of demon worship rotted their culture from within.

Certainly, many xulgath settlements continue to worship demons to this day, paying homage and offering live sacrifices to demons or other terrible creatures from the Outer Rifts. Occasionally, a xulgath mystic can call forth and bind a lesser demon to help serve the group, but one who delves too deep into occultism might summon a more powerful fiend that either tears the xulgaths to pieces or seizes control of the settlement.

```statblock
creature: "Xulgath Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
