---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Puppeteer"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Crafting +15, Occultism +13, Performance +13, Thievery +9"
abilityMods: ["+1", "+2", "+1", "+4", "+1", "+4"]
abilities_top:
  - name: "Puppets"
    desc: "The puppeteer has three animate puppets under their control—a smart puppet, a strong puppet, and a swift puppet. A puppet is a Tiny object that can be share a space with another creature. The usually begin combat in the puppeteer's space. A puppet has AC 23, Hardness 5, 20 Hit Points, and object immunities. If a puppet is destroyed, the puppeteer takes 15 nonlethal mental damage. A puppeteer can rebuild a puppet with 7 days of work. If the puppeteer dies while any of their puppets are still active, the active puppets become independent, but lose the will to fight in their grief."
armorclass:
  - name: AC
    desc: "23; **Fort** +11, **Ref** +14, **Will** +15"
health:
  - name: HP
    desc: "95"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+7 piercing"
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+7 piercing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Manipulate Puppets"
    desc: "`pf2:2` The puppeteer pulls at invisible strings to control their puppets. Each puppet Strides up to 30 feet. Each puppet can then make a Strike as described below. Each attack counts towards the puppeteer's multiple attack penalty, but their penalty does not increase until all attacks have been made. <br>  <br> - **Smart Puppet** The smart puppet is covered in runes that give it occult power. It makes a ranged Strike against a creature within 30 feet at a +15 attack modifier. A successful Strike deals 2d6 mental damage. <br> - **Strong Puppet** The strong puppet wields a tiny sword and shield. It makes a melee Strike against a creature whose space it shares at a +15 attack modifier. A successful Strike deals 2d8 slashing damage. In addition, the strong puppet gains a +1 circumstance bonus to AC for 1 round. <br> - **Swift Puppet** The swift puppet wields two tiny daggers. It makes a melee Strike against a creature whose space it shares at a +15 attack modifier. A successful Strike deals 2d4 piercing damage. If the swift puppet hits a creature that was hit by another puppet this round, its Strike deals an additional 1d4 precision damage. <br>  <br> **Alternative Puppets** <br>  <br> This alternate set of villainous puppets Strikes with a +15 attack modifier. <br>  <br> - **Fiend Puppet** The puppet makes a ranged Strike against a creature within 30 feet for 1d10 spirit damage, plus 1d4 spirit damage if the target is holy. <br> - **Poisoner Puppet** The puppet makes a melee Strike with a tiny syringe of poison against a creature whose space it shares, dealing 1d4 piercing damage plus 1d6 persistent poison damage. <br> - **Undead Puppet** The puppet makes a melee Strike against a creature whose space it shares, dealing 2d8 void damage and making the target [[Frightened]] 1 (or [[Frightened]] 2 on a critical hit)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

On the surface, puppeteers are simply providers of entertainment to the masses. With their little puppets and simple stories, their pantomimes are fun for the whole family. However, some puppeteers have a secret. They can animate their puppets with magic, sending them out to cause all manner of mischief in the dead of night. Puppeteers of this ilk tend to travel by themselves, though they might be found as part of a traveling group if they become lonely. They may serve as an innocent front for more illicit dealings or as lackeys to a larger group of thieves and ne'er do wells.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Puppeteer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
