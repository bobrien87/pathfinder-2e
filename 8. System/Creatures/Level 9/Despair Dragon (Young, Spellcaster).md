---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Despair Dragon (Young, Spellcaster)"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Draconic (Telepathy 60 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +19, Deception +18, Diplomacy +18, Intimidation +20, Occultism +16, Society +16, Stealth +18"
abilityMods: ["+6", "+3", "+2", "+3", "+4", "+5"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Fearsense"
    desc: "The dragon senses all creatures with the frightened condition at the listed range."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +16, **Will** +16"
health:
  - name: HP
    desc: "140; **Immunities** fear effects, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Occult"
    desc: ""
  - name: "Consume Fear"
    desc: "`pf2:r` **Trigger** A creature within 60 feet loses the frightened condition <br>  <br> **Effect** The dragon feasts upon the fear that leaves the triggering creature's body, gaining 4d8 temporary Hit Points that last for 1 minute."
  - name: "Frightful Presence"
    desc: "60 feet. DC 28 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Unbidden Thoughts"
    desc: "`pf2:r` **Trigger** The dragon is critically hit with a weapon or unarmed attack <br>  <br> **Effect** The attacker's mind fills with visions of their worst fears that overwhelm their senses, and they must choose one of the following results: either the triggering attack becomes a normal success, or the critical hit is unaffected but the triggering creature becomes [[Frightened]] 2."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +19 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+12 piercing"
  - name: "Melee strike"
    desc: "Claws +19 (`pf2:1`) (agile, magical), **Damage** 2d8+12 slashing"
  - name: "Melee strike"
    desc: "Tail +17 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d6+10 bludgeoning"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 28, attack +20<br>**4th** (2 slots) [[Darkness]], [[Nightmare]]<br>**3rd** (3 slots) [[Mind Reading]], [[Noise Blast]], [[Slow]]<br>**2nd** (3 slots) [[Paranoia]], [[Stupefy]], [[Ventriloquism]]<br>**1st** (3 slots) [[Command]], [[Ill Omen]], [[Sleep]]<br>**Cantrips** [[Detect Magic]], [[Figment]], [[Haunting Hymn]], [[Message]], [[Telekinetic Projectile]]"
  - name: "Occult Innate Spells"
    desc: "DC 28, attack +20<br>**5th** [[Truespeech]] (Constant)<br>**1st** [[Fear]] (At Will)"
abilities_bot:
  - name: "Shrieking Breath"
    desc: "`pf2:2` The dragon lets out a cacophonous sound made of every scream the dragon has drawn from a terrified enemy, dealing @Damage[8d6[sonic]|options:area-damage] damage in a @Template[type:cone|distance:30] (DC 28 [[Will]] save). Creatures who fail their Will save must spend the first action of their next turn doing nothing but screaming. The dragon can't use Shrieking Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fear is one of the most powerful emotions, and despair dragons are masters of channeling those feelings of terror and hopelessness for their own benefit. As with other occult dragons, despair dragons are driven by an innate compulsion, in their case, the desire to strike terror in others. Despair dragons tend to settle near settlements, so they have a source of fear to draw from. The most common items in despair dragon hoards are scrolls, tomes, and relics that serve as research material. Through these, despair dragons learn of local folklore, urban legends, and more to better haunt their targets.

```statblock
creature: "Despair Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
