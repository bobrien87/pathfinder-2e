---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Omen Dragon (Young, Spellcaster)"
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
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +16, Diplomacy +13, Occultism +17, Society +17, Fortune-Telling Lore +19, Lore (any one subcategory) +17"
abilityMods: ["+5", "+3", "+4", "+6", "+4", "+2"]
abilities_top:
  - name: "Prophetic Wings"
    desc: "The dragon or any ally can glimpse into the future through the dragon's wings in a process that requires 10 minutes of concentration. This casts a 4th-rank [[Augury]] spell, except that the wings can predict results up to 1 day into the future and the dragon always speaks a few cryptic words related to the result of the prediction. <br>  <br> The dragon can use their wings in this way only once per hour, and a given creature can seek a future in the wings only once per week."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +14, **Will** +17"
health:
  - name: HP
    desc: "100; **Immunities** confused, doomed, paralyzed, sleep"
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
    desc: "Jaws +16 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 1d8 mental plus 2d8+5 piercing"
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, magical, unarmed), **Damage** 2d6+5 slashing plus 1d8 mental"
  - name: "Melee strike"
    desc: "Tail +14 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+5 bludgeoning plus 1d8 mental"
  - name: "Melee strike"
    desc: "Wing +14 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 1d8 mental plus 1d8+5 slashing"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 25, attack +17<br>**3rd** (2 slots) [[Dream Message]], [[Hypercognition]]<br>**2nd** (3 slots) [[Clear Mind]], [[Status]], [[Stupefy]]<br>**1st** (3 slots) [[Command]], [[Fear]], [[Protection]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Know the Way]], [[Message]], [[Read Aura]]"
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +17<br>**1st** [[Guidance]], [[Ill Omen]], [[Mindlink]], [[Sure Strike]]"
abilities_bot:
  - name: "Destiny Breath"
    desc: "`pf2:2` The dragon breathes a translucent mist of potentialities that overwhelms creatures with visions of possible features, dealing @Damage[6d6[mental]|options:area-damage] damage in a @Template[cone|distance:20] (DC 25 [[Will]] save). A creature that fails its save is [[Slowed]] 1 for 1 round (or [[Slowed]] 2 on a critical failure) as it struggles with the visions. <br>  <br> The dragon can't use Destiny Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fate is a fickle matter on Golarion. Even with prophecy broken on the world, there are ways to look to the immediate future or acquire a vague sense of long-term events. Omen dragons are bound to see the future—nebulous though it might be—at all times. Visions of the future hound them like a quiet song that never stops playing in their minds. While an omen dragon can focus on or ignore the music of fate at any time, the song plays all the same. At a glance, omen dragons resemble other occult dragons in appearance, save for the mirror-like interior membrane of their wings. An omen dragon's wings offer glimpses into the future. These glimpses are cloudy and vague, but generally correct, if only technically. Omen dragons have a natural compulsion to share the futures they see. These dragons have no compunctions about what the visions show and share their knowledge equally with innocent villagers as they do with wicked tyrants.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Omen Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
