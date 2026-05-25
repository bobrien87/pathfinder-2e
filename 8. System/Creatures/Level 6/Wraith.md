---
type: creature
group: ["Incorporeal", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wraith"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Wraith"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +12, Diplomacy +13, Intimidation +15, Stealth +16"
abilityMods: ["-5", "+4", "+0", "+2", "+2", "+5"]
abilities_top:
  - name: "Void's Embrace"
    desc: "If the victim succeeds at a saving throw against this curse while in sunlight, the curse ends. While you have this curse, you bypass the resistance of the wraith that cursed you. <br>  <br> **Saving Throw** DC 24 [[Will]] save <br>  <br> **Stage 1** the victim is [[Dazzled]] in any light (1 hour) <br>  <br> **Stage 2** the victim gains lifesense 30 feet but is [[Blinded]] in any light (1 hour) <br>  <br> **Stage 3** as stage 2, but the creature also has [[Void Healing]] (1 hour) <br>  <br> **Stage 4** the victim becomes [[Unconscious]] and can't awaken (1 day) <br>  <br> **Stage 5** the creature dies and becomes a wraith, its body crumbling to ash"
armorclass:
  - name: AC
    desc: "24; **Fort** +8, **Ref** +14, **Will** +14"
health:
  - name: HP
    desc: "80; void healing; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed"
abilities_mid:
  - name: "Sunlight Powerlessness"
    desc: "While in sunlight, a wraith is [[Blinded]] and [[Slowed]] 2."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wraith Touch +17 (`pf2:1`) (agile, divine, finesse, void), **Damage** 3d8 void"
spellcasting: []
abilities_bot:
  - name: "Grip of Fear"
    desc: "`pf2:2` The wraith reaches into an adjacent creature's chest, gripping their heart. The target takes 6d6 mental damage with a DC 24 [[Will]] save. On a critical failure, the creature is also [[Paralyzed]] until the start of the wraith's next turn."
  - name: "Robes of Welcome"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The wraith wraps its robes around an adjacent living creature, exposing it to void's embrace. If any creature is cursed by the wraith's void's embrace, the wraith can't impose void's embrace on another creature."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Wraiths are malevolent undead who drain life and shun light. Their shadowy forms are covered by insubstantial robes that they wear like a badge of office and marked with peering eyes that reflect their judgment of the living. A wraith can be created by foul magic or direct exposure to the Void, but more often they are the result of death on a tragic scale. When a tragedy is too great for even reality to witness, a temporary manifestation of the Void can leave behind countless wraiths in a horde of darkness. A wraith's existence is one of emptiness and need, with a desire to call others to the same emptiness exemplified by the Void.

Wraiths can haunt any location where they can safely interact with the living, looking for those worthy to become new wraiths and disposing of the rest, though their vulnerability to sunlight confines them to the shadowy places of the world—places where they can blend in seamlessly with their dark surroundings before silently engulfing their prey. Wraiths' opinions on who is worthy vary, but they typically choose those closest to the Void already, whether from a metaphysical connection or exposure to countless deaths. A new wraith created this way carries these aspects, with the rest of their personality warped or scoured away by exposure to the Void.

Wraiths gather with others of their kind in places where death and mayhem are commonplace—countrysides ravaged by war, metropolitan underworlds run by criminal overlords, or sites of fiendish rituals. In these places, the living do well to keep to the light. Wraiths are smart enough to take advantage of their incorporeality in combat, so they keep to tortuous caverns or structures with hallways, and avoid open areas.

```statblock
creature: "Wraith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
