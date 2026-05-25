---
type: creature
group: ["Amphibious", "Hag"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sea Hag"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Hag"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Aklo, Common, Jotun, Fey, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +11, Deception +10, Occultism +8, Stealth +8"
abilityMods: ["+4", "+3", "+4", "+1", "+3", "+3"]
abilities_top:
  - name: "Coven"
    desc: "A sea hag adds [[Humanoid Form]], [[Mariner's Curse]], and [[Water Walk]] to their coven's spells. Their spell DC when leading a coven is 20. <br>  <br> This monster can form a coven with two or more other creatures who also have the coven ability. This involves performing an 8-hour ceremony with all prospective coven members. After the coven is formed, each of its members gains elite adjustments, adjusting their levels accordingly. Coven members can sense other members' locations and conditions by spending a single action, which has the concentrate trait, and can sense what another coven member is sensing as a two-action activity, which has the concentrate trait as well. <br>  <br> Covens also grant spells and rituals to their members, but these can be cast only in cooperation between three coven members who are all within 30 feet of one another. A coven member can contribute to a coven spell with a single action that has the concentrate trait. If two coven members have contributed these actions within the last round, a third member can cast a coven spell on her turn by spending the normal spellcasting actions. A coven can cast its coven spells an unlimited number of times but can cast only one coven spell each round. All covens grant the 8th-rank [[Cursed Metamorphosis]] spell and all the following spells, which the coven can cast at any rank up to 5th: [[Augury]], [[Charm]], [[Clairaudience]], [[Clairvoyance]], [[Dream Message]], [[Illusory Disguise]], [[Illusory Scene]], [[Scouting Eye]], and [[Talking Corpse]]. Individual creatures with the coven ability also grant additional spells to any coven they join. A coven can also cast the [[Control Weather]] ritual, with a DC of 23 instead of the standard DC. <br>  <br> If a coven member's departure or death brings the coven below three members, the remaining members keep their elite adjustments for 24 hours, but without enough members to contribute the necessary actions, they can't cast coven spells."
  - name: "Sea Hag's Bargain"
    desc: "The sea hag can make a bargain with a willing creature who must be of sound mind. The creature gives away a special or cherished quality—such as its courage, its beauty, or its voice. In exchange, the sea hag spends 1 minute polymorphing the creature into a form the target desires. <br>  <br> This functions as [[Change Shape]]. It might be a total transformation or just changing one or more aspects of the target's body, and it can't make the creature more than one size smaller or larger. The creature changes its Speeds as appropriate for the new form. It doesn't change the attack and damage bonuses with its Strikes, but it might change the damage type the Strikes deal. This has an unlimited duration, and as long as it's transformed, the creature is [[Sickened]] 2 and can't reduce its sickened condition below 2. The creature can slowly and carefully eat and drink despite being sickened. The only way to restore the lost quality used as payment is to defeat the sea hag or make another bargain for its return. Ending the bargain in this way also removes the transformation."
armorclass:
  - name: AC
    desc: "19; **Fort** +11, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "45; **Immunities** polymorph; **Weaknesses** cold iron 3"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, magical, unarmed), **Damage** 1d10+4 slashing"
spellcasting:
  - name: "Coven Spells"
    desc: "DC 20, attack +12<br>**6th** [[Cursed Metamorphosis]]<br>**5th** [[Illusory Scene]], [[Mariner's Curse]], [[Scouting Eye]]<br>**4th** [[Clairvoyance]], [[Talking Corpse]]<br>**3rd** [[Clairaudience]], [[Dream Message]]<br>**2nd** [[Augury]], [[Humanoid Form]], [[Water Walk]]<br>**1st** [[Charm]], [[Illusory Disguise]]"
abilities_bot:
  - name: "Dread Gaze"
    desc: "`pf2:2` The hag gazes upon a creature, afflicting it with a gnawing sense of impending doom, with a result depending on its DC 20 [[Will]] save. The target doesn't need to be able to see the sea hag. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is frightened 1 and is [[Slowed]] 1 for 1 round. If the target was [[Dying]], it remains [[Unconscious]] for 1 day. At the end of the day, it must attempt a DC 20 [[Fortitude]] save against the same DC; if it fails, it dies. <br> - **Critical Failure** As failure, but the creature is [[Frightened]] 2 and slowed 1 for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Sea hags specialize in transformation magic, preying on those who are desperate to change some aspect of their physical appearance. Targets often include those suffering from insecurity about their bodies or those desperate to reside in a different environment, such as aquatic creatures who wish to live on land. These hags are known for tempting desperate victims into tragic and excruciating bargains, though they're also happy to drown and eat mariners who stray too close to their dwellings.

A sea hag has the upper half of a humanoid and the lower half of an octopus, with translucent skin and glowing lights visible beneath their flesh. Sea hags can join covens, but their aquatic nature often prevents them from joining mixed covens with other kinds of hags.

Hags are malevolent predators who use magic and manipulation to lure children and young adults into their clutches. Though their true forms are eldritch and horrifying, hags spend much of their lives disguised as ordinary women. They seek out targets who are unhappy, innocent, or otherwise vulnerable, preying on their weaknesses before snatching them up. The typical hag is abusive, controlling, and narcissistic. Though less malicious hags possibly exist, they rarely reveal their true forms, making them nearly impossible to find.

```statblock
creature: "Sea Hag"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
