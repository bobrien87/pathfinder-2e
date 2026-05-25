---
type: creature
group: ["Hag", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Moon Hag"
level: "10"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Hag"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Aklo, Common, Jotun"
skills:
  - name: Skills
    desc: "Acrobatics +11, Deception +19, Intimidation +17, Occultism +21, Religion +22, Stealth +11"
abilityMods: ["+7", "+5", "+3", "+5", "+6", "+3"]
abilities_top:
  - name: "Coven"
    desc: "A moon hag adds [[Interplanar Teleport]], [[Scrying]], and [[Spirit Blast]] to their coven's spells. <br>  <br> This monster can form a coven with two or more other creatures who also have the coven ability. This involves performing an 8-hour ceremony with all prospective coven members. After the coven is formed, each of its members gains elite adjustments, adjusting their levels accordingly. Coven members can sense other members' locations and conditions by spending a single action, which has the concentrate trait, and can sense what another coven member is sensing as a two-action activity, which has the concentrate trait as well. <br>  <br> Covens also grant spells and rituals to their members, but these can be cast only in cooperation between three coven members who are all within 30 feet of one another. A coven member can contribute to a coven spell with a single action that has the concentrate trait. If two coven members have contributed these actions within the last round, a third member can cast a coven spell on her turn by spending the normal spellcasting actions. A coven can cast its coven spells an unlimited number of times but can cast only one coven spell each round. All covens grant the 8th-rank [[Cursed Metamorphosis]] spell and all the following spells, which the coven can cast at any rank up to 5th: [[Augury]], [[Charm]], [[Clairaudience]], [[Clairvoyance]], [[Dream Message]], [[Illusory Disguise]], [[Illusory Scene]], [[Scouting Eye]], and [[Talking Corpse]]. Individual creatures with the coven ability also grant additional spells to any coven they join. A coven can also cast the [[Control Weather]] ritual, with a DC of 23 instead of the standard DC. <br>  <br> If a coven member's departure or death brings the coven below three members, the remaining members keep their elite adjustments for 24 hours, but without enough members to contribute the necessary actions, they can't cast coven spells."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
armorclass:
  - name: AC
    desc: "28; **Fort** +17, **Ref** +19, **Will** +22"
health:
  - name: HP
    desc: "190"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
  - name: "Moonlight's Kiss"
    desc: "A moon hag in an area illuminated by moonlight gains a +2 status bonus to AC and initiative rolls. In the light of a full moon, they're [[Quickened]], and can use the extra action only to Stride or Strike. If the moon hag has a fly Speed, they can use the extra action to Fly as well."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, magical), **Damage** 2d12+10 slashing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Truespeech]]<br>**4th** [[Confusion]], [[Read Omens]], [[Talking Corpse]]<br>**1st** [[Fear]] (At Will)"
  - name: "Coven Spells"
    desc: "DC 29, attack +21<br>**7th** [[Interplanar Teleport]]<br>**6th** [[Cursed Metamorphosis]], [[Scrying]], [[Spirit Blast]]<br>**5th** [[Illusory Scene]], [[Scouting Eye]]<br>**4th** [[Clairvoyance]], [[Talking Corpse]]<br>**3rd** [[Clairaudience]], [[Dream Message]]<br>**2nd** [[Augury]]<br>**1st** [[Charm]], [[Illusory Disguise]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The moon hag can take on the appearance of any Medium humanoid woman. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Dreadful Prediction"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The moon hag howls a series of dreadful, apocalyptic predictions at a single creature within 30 feet, shattering its perceptions of reality. The target must attempt a DC 29 [[Will]] save and takes a –2 circumstance penalty to the save if it can see the moon. On a failure, the creature becomes [[Stupefied 2]] ([[Stupefied 3]] on a critical failure) until the curse is removed. Regardless of the outcome, the creature is then temporarily immune for 24 hours."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Ride the Moonbeams"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The moon hag teleports themself and any items they're wearing and holding to another space within 30 feet, or 60 feet if they're in moonlight. They then gain a 25-foot fly Speed until the end of their next turn. If the moon hag is in the air when the effect ends, they float to the ground, taking no falling damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Moon hags are powerful soothsayers who use their foresight to sow chaos and misery. Unlike most hags, moon hags typically target the fearful and ambitious, but this is mainly due to such people being easier to manipulate—the fallout from a moon hag's manipulations can destroy families, trigger wars, and ruin nations. A moon hag's true form has chalk white skin, blackened lips, and glowing eyes.

Hags are bizarre predators with uncertain origins, best known for targeting children and the young. To a one, they appear female, and they typically disguise themselves as mortal women in their day-to-day lives. Their powerful magic and manipulative tactics allow them to lure in the naive and vulnerable, exploiting their victims for their own sadistic purposes before kidnapping or devouring them. The typical hag is defined by a vain and controlling nature. Less malevolent hags may exist, but if so, they keep themselves well hidden to avoid the attentions of adventurers and their own abusive kin.

```statblock
creature: "Moon Hag"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
