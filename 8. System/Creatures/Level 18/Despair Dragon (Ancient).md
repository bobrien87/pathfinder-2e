---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Despair Dragon (Ancient)"
level: "18"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+31; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic (Telepathy 90 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +31, Athletics +33, Deception +32, Diplomacy +32, Intimidation +35, Occultism +29, Society +29, Stealth +33"
abilityMods: ["+9", "+5", "+4", "+5", "+5", "+8"]
abilities_top:
  - name: "Telepathy 90 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Fearsense"
    desc: "The dragon senses all creatures with the frightened condition at the listed range."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Shrieking Breath whenever they score a critical hit with a Strike."
  - name: "Tongue Decoy"
    desc: "The despair dragon inflates several bladders at the end of its tongue to create the basic form of a creature. This process takes 1 minute to complete, during which the dragon is [[Off Guard]]. If the dragon stops or is interrupted in this process, the bladders deflate, and the dragon must start over. Once the process is complete, the dragon can maintain the inflated bladders indefinitely, and can Dismiss to deflate the bladders and retract its tongue instantly. <br>  <br> The inflated tongue takes the basic form of an animal or humanoid and can be inflated to be either Small or Medium. The form resembles the general silhouette of a creature, though closer inspection and success at a DC 30 [[Perception]] check can determine the true nature of the tongue. While inflated, the dragon can send its voice through the decoy, though keeping its tongue inflated makes it difficult to speak, causing the dragon to take a –4 circumstance penalty to any checks related to speaking, such as Deception checks to Lie. <br>  <br> The dragon's tongue can extend up to 90 feet from the dragon's body and it can fully extend its tongue as part of the process to inflate the bladders. The dragon can move the inflated part of its tongue up to 15 feet at a time with an action, which has the concentrate, manipulate, and move traits. While extended, the inflated end of the tongue occupies space as a creature of the appropriate size, but the rest of the tongue doesn't impede or block movement in any way. The dragon's scent functions through cilia at the end of the tongue, but otherwise the dragon has no means of knowing what's near its tongue. <br>  <br> Attacking the tongue is the same as attacking the dragon, except that the tongue is always [[Off Guard]]. If the tongue takes any damage, it immediately deflates and remains out. The dragon remains off-guard as long as its tongue is out, but the dragon can retract its tongue with two consecutive Interact actions. If the tongue takes damage, the dragon can't use its tongue decoy again for 1 day."
armorclass:
  - name: AC
    desc: "41; **Fort** +28, **Ref** +30, **Will** +32"
health:
  - name: HP
    desc: "325; **Immunities** fear effects, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Occult"
    desc: ""
  - name: "Consume Fear"
    desc: "`pf2:r` **Trigger** A creature within 60 feet loses the frightened condition <br>  <br> **Effect** The dragon feasts upon the fear that leaves the triggering creature's body, gaining 7d8 temporary Hit Points that last for 1 minute."
  - name: "Frightful Presence"
    desc: "60 feet. DC 40 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Unbidden Thoughts"
    desc: "`pf2:r` **Trigger** The dragon is critically hit with a weapon or unarmed attack <br>  <br> **Effect** The attacker's mind fills with visions of their worst fears that overwhelm their senses, and they must choose one of the following results: either the triggering attack becomes a normal success, or the critical hit is unaffected but the triggering creature becomes [[Frightened]] 2."
  - name: "Look Behind You"
    desc: "`pf2:0` **Trigger** The dragon successfully Hides from a creature within 90 feet <br>  <br> **Effect** The dragon teleports to a space directly behind the target creature. The dragon immediately becomes detected unless their chosen position has cover or another means to remain [[Hidden]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +33 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d12+20 piercing"
  - name: "Melee strike"
    desc: "Claws +33 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 3d10+20 slashing"
  - name: "Melee strike"
    desc: "Tail +31 (`pf2:1`) (magical, reach 25 ft.), **Damage** 3d8+18 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40, attack +32<br>**5th** [[Truespeech]] (Constant), [[Wave of Despair]]<br>**1st** [[Fear]] (At Will)"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Shrieking Breath"
    desc: "`pf2:2` The dragon lets out a cacophonous sound made of every scream the dragon has drawn from a terrified enemy, dealing @Damage[17d6[sonic]|options:area-damage] damage in a @Template[type:cone|distance:50] (DC 40 [[Will]] save). Creatures who fail their Will save must spend the first action of their next turn doing nothing but screaming. The dragon can't use Shrieking Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fear is one of the most powerful emotions, and despair dragons are masters of channeling those feelings of terror and hopelessness for their own benefit. As with other occult dragons, despair dragons are driven by an innate compulsion, in their case, the desire to strike terror in others. Despair dragons tend to settle near settlements, so they have a source of fear to draw from. The most common items in despair dragon hoards are scrolls, tomes, and relics that serve as research material. Through these, despair dragons learn of local folklore, urban legends, and more to better haunt their targets.

```statblock
creature: "Despair Dragon (Ancient)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
