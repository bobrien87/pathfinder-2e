---
type: creature
group: ["Rakshasa", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Raktavarna"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Rakshasa"
trait_02: "Spirit"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Common, Diabolic, Sakvroth, Chthonian, Empyrean"
skills:
  - name: Skills
    desc: "Athletics +6, Deception +7, Diplomacy +7, Stealth +7"
abilityMods: ["+1", "+4", "+2", "+1", "+1", "+2"]
abilities_top:
  - name: "Betraying Bite"
    desc: "A raktavarna gains a +2 bonus to Strikes against any creature that is holding it."
  - name: "Designate Master"
    desc: "The raktavarna spends 10 minutes on an invocation alongside another creature. That creature becomes the raktavarna's master until the raktavarna dies or Dismisses the effect. The master gains the Master's Eyes activity as long as the bond lasts. <br>  <br> [[Master's Eye]]"
  - name: "Raktavarna Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 1d4 poison damage and [[Stupefied 2]] (1 round)"
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "20; **Weaknesses** holy 3"
abilities_mid:
  - name: "+2 Status to All Saves vs. Divine Magic"
    desc: ""
  - name: "Knowledge of Delusion"
    desc: "A creature that fails a Recall Knowledge check or a Perception check to [[Sense Motive]] on a rakshasa is [[Off Guard]] until the end of its next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +9 (`pf2:1`) (agile, finesse, reach 0 ft., unholy), **Damage** 1d6+1 piercing plus [[Raktavarna Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16, attack +8<br>**4th** [[Read Omens]]<br>**1st** [[Charm]], [[Command]], [[Detect Magic]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The raktavarna takes on the appearance of a Tiny inanimate object. If, while transformed, the raktavarna takes any action other than the purely mental (such as Recall Knowledge), they immediately revert to their original form. Until then, they can use Deception to Impersonate the object. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Raktavarnas are simple rakshasa incarnations of betrayal and assassination, often existing to test the mettle of those who were treacherous or poisonous in a previous life. They typically appear as a snake with blood-red eyes and oversized fangs, though they just as often appear in the guise of a sword or a piece of jewelry.

Rakshasas are primordial, divine beings who serve as incarnations of all that is foul within creation, born the moment that the concepts of good and evil were first conceived. It is their divine purpose to exemplify the profane—by murdering their own kin, eating the flesh of sapient beings, and performing thousands of other atrocities, they define these acts as obscene and taboo, so that mortals know these acts to be crimes in the eyes of the holy. It is a role they must play, in the same way that a stage play must have an actor to serve as the villain, a role that damned all rakshasas from the moment of their genesis.

Most rakshasas enjoy their role, in the same way an actor enjoys delivering a masterful performance, yet there is an element of tragedy to their existence. They are fated to serve solely as foils to others, to corrupt the unworthy and fall to the heroic, never free to forge their own path. They are condemned to perform the most heinous of deeds, even if it rankles their sensibilities and conscience. To do otherwise is to defy their nature and their purpose: the greatest sin a rakshasa can perform.

```statblock
creature: "Raktavarna"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
