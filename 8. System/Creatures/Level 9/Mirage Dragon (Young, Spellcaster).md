---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mirage Dragon (Young, Spellcaster)"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +19, Arcana +19, Athletics +18, Crafting +19, Deception +21, Diplomacy +19, Performance +19, Stealth +19, Thievery +19, Illusion Lore +21"
abilityMods: ["+5", "+4", "+3", "+4", "+5", "+6"]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can Hide in natural environments even if they don't have cover."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to [[Off Guard]] targets."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +17, **Will** +20"
health:
  - name: HP
    desc: "155; **Immunities** fascinated, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Scintillating Defense"
    desc: "`pf2:r` **Trigger** The dragon is targeted with an attack <br>  <br> **Effect** The dragon flashes their iridescent scales at the triggering creature to throw off the attack. The dragon gains [[Concealment]] against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d10+8 piercing"
  - name: "Melee strike"
    desc: "Claws +20 (`pf2:1`) (agile, magical), **Damage** 2d6+8 slashing"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+8 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 27, attack +20<br>**4th** (2 slots) [[Confusion]], [[Vision of Death]]<br>**3rd** (3 slots) [[Disguise Magic]], [[Enthrall]], [[Hypnotize]]<br>**2nd** (3 slots) [[Embed Message]], [[Revealing Light]], [[See the Unseen]]<br>**1st** (3 slots) [[Item Facade]], [[Phantasmal Minion]], [[Ventriloquism]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Light]], [[Prestidigitation]], [[Read Aura]]"
  - name: "Arcane Innate Spells"
    desc: "DC 27, attack +19<br>**5th** [[Illusory Scene]]<br>**4th** [[Mirage]]<br>**2nd** [[Illusory Creature]], [[Invisibility]]<br>**1st** [[Figment]], [[Illusory Object]] (At Will), [[Message]]"
abilities_bot:
  - name: "Hallucinatory Breath"
    desc: "`pf2:2` The dragon breathes a cloud that assaults the senses and deals @Damage[7d6[mental]|options:area-damage] damage in a @Template[cone|distance:30] (DC 27 [[Will]] save). A creature that fails its save is also [[Confused]] for 1 round (1 minute on a critical failure) and is then temporarily immune to being confused by Hallucinatory Breath for 1 hour. <br>  <br> The dragon can't use Hallucinatory Breath again for 1d4 rounds."
  - name: "Lunging Bite"
    desc: "`pf2:2` The dragon lunges their head forward, making a jaws Strike with an extended reach of 20 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Mirage dragons are masters of illusion magic and use their powers to deceive others and further their own agendas. In addition to their magical prowess, mirage dragons possess a number of additional features to help them on hunts or mislead attackers, such as their camouflaging scales and a hallucinatory breath that can confound multiple foes at once. Mirage dragons are vain and egotistical figures. They ultimately care more about themselves than others.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Mirage Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
