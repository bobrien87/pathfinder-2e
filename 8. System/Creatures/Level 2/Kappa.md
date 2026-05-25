---
type: creature
group: ["Amphibious", "Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kappa"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +7, Medicine +9, Survival +7"
abilityMods: ["+3", "+4", "+1", "+1", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "Head Bowl"
    desc: "The depression atop a kappa's head is filled with water. Spilling, evaporating, or otherwise removing all the water from the top of a kappa's head reduces all their Speeds to 5 feet until the basin is again filled with water. A kappa who becomes [[Prone]] must succeed at a DC 15 [[Reflex]] save or spill their water, and a kappa who becomes [[Unconscious]] automatically spills their water. <br>  <br> If a kappa is [[Grabbed]], [[Restrained]], or stunned, another creature can attempt to spill the water from their bowl by spending a single action, which has the attack and manipulate traits, to attempt an Athletics check against the kappa's Fortitude DC. On a success, the creature spills the kappa's water."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile), **Damage** 1d10+3 slashing"
spellcasting: []
abilities_bot:
  - name: "Pull Arm"
    desc: "`pf2:1` The kappa pulls one of their arms, gaining 10-foot reach with that arm. The opposing arm shrinks to little more than a hand extending from their shell. The kappa can still use their shortened hand to hold things, but they can't use that hand to wield a shield or weapon. By spending a single action to pull their opposing arm, the kappa can return their arms to their original length."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Mischievous by nature, kappas delight in playing pranks on unsuspecting travelers. While usually not overtly malicious, they can be a significant nuisance, stealing clothes from unsuspecting bathers or snatching unattended food from campfires. Kappas also enjoy proving their worth in competitions of strength and, despite their propensity for trickery, are known to be honorable competitors who keep their word and remain polite in conversation.

While kappas vary in physical attributes from region to region, they're all amphibious, turtle-like humanoids with beaked mouths, webbed hands and feet, and slimy scales that range in color from bluish green to pale yellow. They often have black hair, arranged in a ring to accommodate the central depression atop their head. Water from a kappa's home lake, stream, or river fills this depression, or head bowl, which is believed to be the source of their strength. Younger kappas are easily tricked into bowing and accidentally emptying the water from their own head bowls. Losing this water makes a kappa lethargic. The longer a kappa's head bowl remains empty, the weaker they grow. While this rarely poses a serious danger for a kappa living near their home body of water, it can prove fatal to a more adventurous kappa wandering afar.

Kappas aren't inherently hostile and have been known to befriend lonely children and lend aid to stranded adventurers by providing directions or minor medical treatment. Still, many areas where kappas dwell feature posted signs warning of their presence that encourage travelers venturing near water to toss in a cucumber—kappas' favorite food—in exchange for safe passage. Kappas sometimes put up these signs themselves to increase the likelihood of receiving a tasty treat.

```statblock
creature: "Kappa"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
