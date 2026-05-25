---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Whisper Dragon (Ancient, Spellcaster)"
level: "16"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean, Fey (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +27, Athletics +29, Deception +28, Diplomacy +30, Intimidation +28, Occultism +31, Society +35, Stealth +29, Underworld Lore +33"
abilityMods: ["+7", "+5", "+6", "+9", "+6", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Information Network"
    desc: "The dragon can attempt a Society check to [[Recall Knowledge]] in place of a check to Gather Information, recalling intelligence from prior informants."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "39; **Fort** +28, **Ref** +26, **Will** +30"
health:
  - name: HP
    desc: "290; **Immunities** confused, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Occult"
    desc: ""
  - name: "Diplomatic Solution"
    desc: "`pf2:0` **Trigger** The dragon rolls initiative <br>  <br> **Effect** The dragon targets all enemies it can see within @Template[emanation|distance:60]{60 feet} with [[Calm]] heightened to a rank equal to half the dragon's level rounded up (DC 35 [[Will]] save). The dragon doesn't need to Sustain this effect, but if the dragon takes any hostile action against those affected, it breaks the effect for all creatures."
  - name: "Distracting Whisper"
    desc: "`pf2:r` **Trigger** The dragon is targeted with an attack <br>  <br> **Effect** A mysterious voice whispers something disconcerting in the triggering creature's ear, inflicting a –2 circumstance penalty to the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +32 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d12+15 piercing"
  - name: "Melee strike"
    desc: "Claw +32 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d10+15 slashing"
  - name: "Melee strike"
    desc: "Tail +30 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d10+15 bludgeoning"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 37, attack +29<br>**7th** (3 slots) [[Interplanar Teleport]], [[Project Image]], [[Retrocognition]]<br>**6th** (3 slots) [[Scrying]], [[Teleport]], [[Zealous Conviction]]<br>**5th** (3 slots) [[Sending]], [[Synaptic Pulse]], [[Scouting Eye]]<br>**4th** (3 slots) [[Confusion]], [[Detect Scrying]], [[Rewrite Memory]]<br>**3rd** (3 slots) [[Hypercognition]], [[Ring of Truth]], [[Dream Message]]<br>**2nd** (3 slots) [[Clear Mind]], [[Humanoid Form]], [[See the Unseen]]<br>**1st** (3 slots) [[Command]], [[Disguise Magic]], [[Mindlink]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Forbidding Ward]], [[Message]], [[Telekinetic Hand]]"
  - name: "Occult Innate Spells"
    desc: "DC 37, attack +0<br>**8th** [[Hidden Mind]] (Constant)<br>**7th** [[Retrocognition]]<br>**5th** [[Mind Probe]]<br>**4th** [[Clairvoyance]] (At Will), [[Suggestion]]<br>**3rd** [[Clairaudience]] (At Will), [[Mind Reading]], [[Ring of Truth]]<br>**2nd** [[Embed Message]]<br>**1st** [[Charm]], [[Daze]], [[Message]]"
abilities_bot:
  - name: "Cogitation Breath"
    desc: "`pf2:2` The dragon unleashes a befuddling miasma, dealing @Damage[15d6[mental]|options:area-damage] damage in a @Template[type:cone|distance:50] (DC 37 [[Will]] save). A creature that fails its save is [[Stupefied 1]] ([[Stupefied 2]] on a critical failure) for 1 minute. The dragon can't use Cogitation Breath again for 1d4 rounds."
  - name: "Steal Knowledge"
    desc: "`pf2:1` The dragon plucks a fragment of knowledge from the mind of a creature within 60 feet, choosing a skill to affect. The creature must attempt a DC 35 [[Will]] save. <br> - **Success** The creature is unaffected. <br> - **Failure** For the next minute, the creature takes a –1 status penalty to checks using that skill, and the dragon gets a +1 status bonus to using that skill. <br> - **Critical Failure** As failure, but the penalty is –2 and the bonus is +2."
  - name: "Thought Whispers"
    desc: "`pf2:2` **Frequency** once per minute <br>  <br> **Effect** The dragon sends their mind out to seek others' thoughts, affecting all creatures within 60 feet with mind reading (DC 37 [[Will]] save)."
  - name: "Unveil Secret"
    desc: "`pf2:2` The dragon delves into the mind of a creature within 60 feet to scour for secrets, learning something the creature would find embarrassing or shameful unless they succeed a DC 37 [[Will]] save. The target becomes [[Frightened]] 1 and can't reduce their frightened condition for 1 minute or until the dragon reveals the secret. As a reaction when the affected creature attempts a check, the dragon can reveal their secret to discomfit them, requiring them to roll twice and take the lower result; this is a misfortune effect."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Whisper dragons are keen collectors of rumors and secrets who spend centuries honing their information networks and relationships. They generally do so not out of an intent to hold the information over others or to use for their own machinations, but simply because the process of learning and gathering information is fulfilling. Their hoards are sparse compared to those of other dragons, as they hold their true treasures—secrets—in their minds.

```statblock
creature: "Whisper Dragon (Ancient, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
