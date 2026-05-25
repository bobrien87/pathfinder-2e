---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Omen Dragon (Ancient, Spellcaster)"
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
    desc: "+29; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Fey, Jotun, Aklo"
skills:
  - name: Skills
    desc: "Acrobatics +28, Athletics +30, Diplomacy +29, Occultism +33, Society +31, Fortune-Telling Lore +33, Lore (any one subcategory) +31"
abilityMods: ["+8", "+6", "+7", "+9", "+7", "+5"]
abilities_top:
  - name: "Impending Fate"
    desc: "The dragon's attacks bring their foes closer to their eventual fates. When the dragon critically hits with a Strike or a creature critically fails against the dragon's Destiny Breath, the creature becomes [[Doomed]] 1, or increases its doomed value by 1 if it was already doomed."
  - name: "Prophetic Wings"
    desc: "The dragon or any ally can glimpse into the future through the dragon's wings in a process that requires 10 minutes of concentration. This casts a 8th-rank [[Augury]] spell, except that the wings can predict results up to 1 year into the future and the dragon always speaks a few cryptic words related to the result of the prediction. <br>  <br> The dragon can use their wings in this way only once per day, and a given creature can seek a future in the wings only once per week."
armorclass:
  - name: AC
    desc: "38; **Fort** +27, **Ref** +28, **Will** +29"
health:
  - name: HP
    desc: "280; **Immunities** confused, doomed, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Occult"
    desc: ""
  - name: "Challenge Fate"
    desc: "`pf2:r` **Trigger** The dragon is targeted by an attack; <br>  <br> **Effect** This fate is not set in stone. The attacker rolls the triggering attack twice and uses the worse result."
  - name: "Untethered to Fate"
    desc: "The dragon can choose to negate any fortune or misfortune effects that would affect them; other creatures remain affected normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +30 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 1d8 mental plus 3d8+14 piercing"
  - name: "Melee strike"
    desc: "Claw +30 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 3d6+14 slashing plus 1d8 mental"
  - name: "Melee strike"
    desc: "Tail +28 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d8+14 bludgeoning plus 1d8 mental"
  - name: "Melee strike"
    desc: "Wing +28 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 1d8 mental plus 2d8+14 slashing"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 39, attack +31<br>**7th** (3 slots) [[Never Mind]], [[Visions of Danger]], [[Warp Mind]]<br>**6th** (3 slots) [[Repulsion]], [[Scrying]], [[Truesight]]<br>**5th** (3 slots) [[Locate]], [[Wave of Despair]], [[Sending]]<br>**4th** (3 slots) [[Clairvoyance]], [[Confusion]], [[Read Omens]]<br>**3rd** (3 slots) [[Dream Message]], [[Hypercognition]], [[Locate]]<br>**2nd** (3 slots) [[Clear Mind]], [[Status]], [[Stupefy]]<br>**1st** (3 slots) [[Command]], [[Fear]], [[Protection]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Know the Way]], [[Message]], [[Read Aura]]"
  - name: "Occult Innate Spells"
    desc: "DC 39, attack +31<br>**7th** [[Retrocognition]], [[True Target]]<br>**1st** [[Guidance]], [[Ill Omen]] (At Will), [[Mindlink]] (At Will)"
abilities_bot:
  - name: "Destiny Breath"
    desc: "`pf2:2` The dragon breathes a translucent mist of potentialities that overwhelms creatures with visions of possible features, dealing @Damage[15d6[mental]|options:area-damage] damage in a @Template[cone|distance:40] (DC 39 [[Will]] save). A creature that fails its save is [[Slowed]] 1 for 1 round (or [[Slowed]] 2 on a critical failure) as it struggles with the visions. <br>  <br> The dragon can't use Destiny Breath again for 1d4 rounds."
  - name: "Walk the Timelines"
    desc: "`pf2:2` **Frequency** once per hour <br>  <br> **Effect** The dragon splits themself into two versions with different fates. Each copy Strides or Flies from the dragon's current space, then takes a single action. If the actions are both attacks, they use the same multiple attack penalty and count as one attack toward the dragon's multiple attack penalty. <br>  <br> After both actions, the dragon chooses one of the two locations as their actual destination and the other version of themself disappears."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fate is a fickle matter on Golarion. Even with prophecy broken on the world, there are ways to look to the immediate future or acquire a vague sense of long-term events. Omen dragons are bound to see the future—nebulous though it might be—at all times. Visions of the future hound them like a quiet song that never stops playing in their minds. While an omen dragon can focus on or ignore the music of fate at any time, the song plays all the same. At a glance, omen dragons resemble other occult dragons in appearance, save for the mirror-like interior membrane of their wings. An omen dragon's wings offer glimpses into the future. These glimpses are cloudy and vague, but generally correct, if only technically. Omen dragons have a natural compulsion to share the futures they see. These dragons have no compunctions about what the visions show and share their knowledge equally with innocent villagers as they do with wicked tyrants.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Omen Dragon (Ancient, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
