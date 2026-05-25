---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Drill Sergeant"
level: "8"
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
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +20, Warfare Lore +18"
abilityMods: ["+4", "+3", "+2", "+2", "+2", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +14, **Ref** +15, **Will** +20"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Commanding Aura"
    desc: "60 feet. An ally that starts its turn in the aura gains 8 temporary Hit Points. These last until the start of the creature's next turn. <br>  <br> > [!danger] Effect: Commanding Aura"
  - name: "You Don't Have My Permission to Die!"
    desc: "`pf2:r` **Trigger** An allied creature within 30 feet would be reduced to 0 Hit Points <br>  <br> **Effect** With a stern rebuke, the drill sergeant berates the target for their failure. The creature avoids being knocked out and remains at 1 HP. The creature is then temporarily immune for 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Javelin +19 (`pf2:1`) (thrown 30), **Damage** 1d6+12 piercing"
  - name: "Melee strike"
    desc: "Longsword +21 (`pf2:1`) (magical, versatile p), **Damage** 2d8+12 slashing"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Chastising Enforcement"
    desc: "`pf2:1` The drill sergeant exhorts a faltering comrade with a stern word and attempts an [[Intimidation]] check against the Will DC of one ally within 30 feet. On a success, the target's [[Frightened]] condition is reduced by 2 and the drill sergeant can attempt to counteract one mental effect that ally is suffering from with a +18 counteract modifier. On a critical success, the drill sergeant also reduces the frightened condition of each other ally in a @Template[type:emanation|distance:10] around the target by 1."
  - name: "Keep Up With Me!"
    desc: "`pf2:1` **Requirements** The drill sergeant's last action was a Strike that hit <br>  <br> **Effect** The drill sergeant shouts that one ally within 30 feet can't keep up with them. That ally gains a +3 status bonus to their attack roll on the next Strike they make before the start of the drill sergeant's next turn. If the ally is a troop, this bonus instead applies to the DC of their next offensive activity (such as Join the Fray for heavy cavalry). <br>  <br> > [!danger] Effect: Keep Up With Me!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Maintaining discipline is of the utmost importance when conducting a military campaign. Often elevated from veteran soldiers, drill sergeants are responsible for training common troops, ensuring they can follow orders and fight well in the thick of battle. Though drill sergeants can be brash and hard-nosed, harsh discipline is often crucial to maintaining order and keeping soldiers alive.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Drill Sergeant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
