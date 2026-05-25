---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gadgeteer"
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
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +16, Society +12, Thievery +14, Engineering Lore +18"
abilityMods: ["+1", "+4", "+1", "+4", "+2", "+0"]
abilities_top:
  - name: "Gadget Specialist"
    desc: "For encounters involving crafting gadgets, the gadgeteer is a 9th-level challenge."
armorclass:
  - name: AC
    desc: "23; **Fort** +11, **Ref** +16, **Will** +14"
health:
  - name: HP
    desc: "95"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
  - name: "Melee strike"
    desc: "Heavy Wrench +16 (`pf2:1`) (shove), **Damage** 1d6+7 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +16 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Create Gadget"
    desc: "`pf2:3` The gadgeteer uses their bag of junk and nearby scraps to create one of the following gadgets. Gadgets created this way fall apart after a single use or after 1 hour, whichever happens first. <br>  <br> - **Flash Bang** `pf2:1` (manipulate) The gadgeteer throws a flash bang up to 20 feet away that explodes in a @Template[type:burst|distance:5]. Creatures in the burst must succeed a DC 24 [[Fortitude]] save or become [[Blinded]] for 1 round. <br> - **Glider** `pf2:1` (move) The gadgeteer leaps off a precipice with the glider in their hands. They fall only 60 feet per round, and for every 10 feet they fall, they can travel 5 feet forward. <br> - **Makeshift Key** `pf2:1` (manipulate) The gadgeteer attempts to Pick a Lock with a +4 item bonus to the check. <br> - **Recorder** `pf2:1` (manipulate) The gadgeteer records up to 25 spoken words on this device. Activating this gadget causes it to either repeat the recorded words once before falling apart or play the message on a loop for up to 10 minutes before falling apart. <br> - **Shocking Rod** `pf2:1` (manipulate) An adjacent creature takes 3d12 electricity damage with a DC 24 [[Reflex]] save."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Few are as prepared to be unprepared as a gadgeteer, who are masters at building seemingly impossible creations out of almost anything. They're always useful to have when a plan inevitably goes wrong because they can quickly craft the perfect tool needed to get out of even the stickiest predicament. Every now and again, someone tries to hire a gadgeteer to perfect a single design to replicate it and make more permanent versions of their thrown-together gadgets. This effort is often in vain, as even the most talented gadgeteers are unlikely to perfectly replicate a design they made in the moment, even with the same materials. In fact, when put on the spot, they will likely create a functional gadget differently every time, even if they have access to the same material. This process makes duplication nearly impossible.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Gadgeteer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
