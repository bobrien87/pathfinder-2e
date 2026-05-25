---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Artillerist"
level: "3"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +9, Diplomacy +9, Society +9, Thievery +8, Engineering Lore +11, Explosive Lore +9"
abilityMods: ["+3", "+3", "+1", "+2", "+1", "+0"]
abilities_top:
  - name: "Siege Acumen"
    desc: "The artillerist is permanently quickened. They can use this extra action only to Aim, Load, or Launch a siege weapon."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +12, **Will** +6"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Siege Shield"
    desc: "While adjacent to a siege weapon, the artillerist gains a +1 circumstance bonus to AC."
  - name: "Siege Weapons Expert"
    desc: "The artillerist gains a +2 bonus to [[Perception]] check if the artillerist is crewing a siege weapon. Additionally, they gain a +2 bonus to Engineering lore check and Explosive lore check for siege weapons."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +10 (`pf2:1`) (agile), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +10 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Dueling Pistol +10 (`pf2:1`) (concealable, concussive, fatal d10, reload 1, range 60 ft.), **Damage** 1d6+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Bombard"
    desc: "`pf2:2` The artillerist activates a shoulder-mounted artillery piece to launch an explosive shell up to 120 feet away that explodes in @Template[type:burst|distance:10]. Creatures within the burst take @Damage[2d6[piercing],2d6[fire]|options:area-damage] damage with a DC 19 [[Reflex]] save. A creature that fails its save is also knocked [[Prone]]. The artillerist can't use Bombard again until they reload the artillery with 2 Interact actions; these actions don't have to be consecutive."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The maintenance and operation of a siege weapon is the highest form of art for the artillerist. They are second to none in terms of reliability and speed due to years of experience and training. Their mastery is such that they often construct smaller models of their preferred weapon to mount on their shoulders. Many will insist this is in case of an emergency, but they often truly enjoy crafting, designing, and perfecting their personal piece of artillery. Traditionally, artillerists are used on both side of a siege. Massive weapons are both fired towards the walls and from the walls. In such battles, artillerists are invaluable. However, artillerists are seen in other places outside of massive wars. For example, artillerists are often employed on ships to manage their cannons and harpoons.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Artillerist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
