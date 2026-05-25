---
type: creature
group: ["Hag", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Iron Hag"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Hag"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Aklo, Common, Jotun"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +14, Deception +13, Diplomacy +11, Intimidation +13, Stealth +16"
abilityMods: ["+6", "+4", "+4", "+1", "+4", "+3"]
abilities_top:
  - name: "Coven"
    desc: "An iron hag adds [[Earthbind]], [[Impaling Spike]], and [[Spellwrack]] to their coven's spells. Their spell DC when leading a coven is 24. <br>  <br> This monster can form a coven with two or more other creatures who also have the coven ability. This involves performing an 8-hour ceremony with all prospective coven members. After the coven is formed, each of its members gains elite adjustments, adjusting their levels accordingly. Coven members can sense other members' locations and conditions by spending a single action, which has the concentrate trait, and can sense what another coven member is sensing as a two-action activity, which has the concentrate trait as well. <br>  <br> Covens also grant spells and rituals to their members, but these can be cast only in cooperation between three coven members who are all within 30 feet of one another. A coven member can contribute to a coven spell with a single action that has the concentrate trait. If two coven members have contributed these actions within the last round, a third member can cast a coven spell on her turn by spending the normal spellcasting actions. A coven can cast its coven spells an unlimited number of times but can cast only one coven spell each round. All covens grant the 8th-rank [[Cursed Metamorphosis]] spell and all the following spells, which the coven can cast at any rank up to 5th: [[Augury]], [[Charm]], [[Clairaudience]], [[Clairvoyance]], [[Dream Message]], [[Illusory Disguise]], [[Illusory Scene]], [[Scouting Eye]], and [[Talking Corpse]]. Individual creatures with the coven ability also grant additional spells to any coven they join. A coven can also cast the [[Control Weather]] ritual, with a DC of 23 instead of the standard DC. <br>  <br> If a coven member's departure or death brings the coven below three members, the remaining members keep their elite adjustments for 24 hours, but without enough members to contribute the necessary actions, they can't cast coven spells."
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "80; **Resistances** physical 3 except adamantine"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, cold iron, magical, reach 10 ft., unarmed), **Damage** 2d8+6 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (cold iron, magical, unarmed), **Damage** 2d6+6 piercing"
spellcasting:
  - name: "Coven Spells"
    desc: "DC 24, attack +16<br>**6th** [[Cursed Metamorphosis]], [[Spellwrack]]<br>**5th** [[Illusory Scene]], [[Impaling Spike]], [[Scouting Eye]]<br>**4th** [[Clairvoyance]], [[Talking Corpse]]<br>**3rd** [[Clairaudience]], [[Dream Message]], [[Earthbind]]<br>**2nd** [[Augury]]<br>**1st** [[Charm]], [[Illusory Disguise]]"
abilities_bot:
  - name: "Bonds of Iron"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The hag causes a cage built of cold iron fingernails to spring out of nothingness around one creature within 30 feet, attempting an Athletics check to `act grapple` against the target's Fortitude DC; if the target has a weakness to cold iron, the iron hag gains a +2 circumstance bonus to this check. <br>  <br> On a success, the creature is [[Grabbed]] by the magical fingernails (or [[Restrained]] on a critical success). If the creature successfully Escapes, the cage crumbles into rust. <br>  <br> Any creature can attempt to destroy the cage by attacking it. It has an AC of 19, Hardness 10, and 40 Hit Points."
  - name: "Change Shape"
    desc: "`pf2:1` The iron hag can take on the appearance of any Medium female humanoid. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Embrace of Iron"
    desc: "`pf2:1` **Requirements** A creature is [[Grabbed]] or [[Restrained]] by the iron hag's claw <br>  <br> **Effect** The hag's nails tear into their captured victim, dealing @Damage[2d8[piercing]|traits:cold-iron] damage (the nails are cold iron). Then the hag can attempt to [[Reposition]] the creature. If the creature is adjacent to the hag, they can then attempt a jaws Strike against it."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Iron hags are kidnappers, targeting those too young to even remember to fight back. They most often snatch babies from their cradles, though they sometimes target fearful children or youths who suffer from anxiety. They then imprison their new wards in towers or enchanted dungeons, terrifying their victims with stories of the outside world to discourage them from even trying to escape. If these methods fail to be effective, iron hags become more straightforward in their methods of imprisonment, insisting it's for their captives' own good.

An iron hag's true form has unnaturally long arms. True to their name, they have teeth made of iron, as well as long iron toenails and claws.

Hags are malevolent predators who use magic and manipulation to lure children and young adults into their clutches. Though their true forms are eldritch and horrifying, hags spend much of their lives disguised as ordinary women. They seek out targets who are unhappy, innocent, or otherwise vulnerable, preying on their weaknesses before snatching them up. The typical hag is abusive, controlling, and narcissistic. Though less malicious hags possibly exist, they rarely reveal their true forms, making them nearly impossible to find.

```statblock
creature: "Iron Hag"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
