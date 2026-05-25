---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Whisper Dragon (Young)"
level: "7"
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
    desc: "+15; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean, Fey (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +14, Deception +13, Diplomacy +15, Intimidation +13, Occultism +15, Society +17, Stealth +14, Underworld Lore +17"
abilityMods: ["+4", "+2", "+3", "+3", "+2", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Information Network"
    desc: "The dragon can attempt a Society check to [[Recall Knowledge]] in place of a check to Gather Information, recalling intelligence from prior informants."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Cogitation Breath whenever they score a critical hit with a Strike."
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +13, **Will** +18"
health:
  - name: HP
    desc: "110; **Immunities** confused, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status To All Saves Vs. Occult"
    desc: ""
  - name: "Diplomatic Solution"
    desc: "`pf2:0` **Trigger** The dragon rolls initiative <br>  <br> **Effect** The dragon targets all enemies it can see within @Template[emanation|distance:60]{60 feet} with [[Calm]] heightened to a rank equal to half the dragon's level rounded up (DC 23 [[Will]] save). The dragon doesn't need to Sustain this effect, but if the dragon takes any hostile action against those affected, it breaks the effect for all creatures."
  - name: "Distracting Whisper"
    desc: "`pf2:r` **Trigger** The dragon is targeted with an attack <br>  <br> **Effect** A mysterious voice whispers something disconcerting in the triggering creature's ear, inflicting a –2 circumstance penalty to the triggering attack. <br>  <br> > [!danger] Effect: Distracting Whisper"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+6 piercing"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, magical), **Damage** 2d8+6 slashing"
  - name: "Melee strike"
    desc: "Tail +16 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+6 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +0<br>**4th** [[Clairvoyance]] (At Will), [[Suggestion]]<br>**3rd** [[Clairaudience]] (At Will)<br>**2nd** [[Embed Message]]<br>**1st** [[Charm]], [[Daze]], [[Message]]"
abilities_bot:
  - name: "Cogitation Breath"
    desc: "`pf2:2` The dragon unleashes a befuddling miasma, dealing @Damage[6d6[mental]|options:area-damage] damage in a @Template[type:cone|distance:30] (DC 25 [[Will]] save). A creature that fails its save is [[Stupefied 1]] ([[Stupefied 2]] on a critical failure) for 1 minute. The dragon can't use Cogitation Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Steal Knowledge"
    desc: "`pf2:1` The dragon plucks a fragment of knowledge from the mind of a creature within 60 feet, choosing a skill to affect. The creature must attempt a DC 23 [[Will]] save. <br> - **Success** The creature is unaffected. <br> - **Failure** For the next minute, the creature takes a –1 status penalty to checks using that skill, and the dragon gets a +1 status bonus to using that skill. <br> - **Critical Failure** As failure, but the penalty is –2 and the bonus is +2."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Whisper dragons are keen collectors of rumors and secrets who spend centuries honing their information networks and relationships. They generally do so not out of an intent to hold the information over others or to use for their own machinations, but simply because the process of learning and gathering information is fulfilling. Their hoards are sparse compared to those of other dragons, as they hold their true treasures—secrets—in their minds.

```statblock
creature: "Whisper Dragon (Young)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
